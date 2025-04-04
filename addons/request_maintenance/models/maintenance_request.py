import ast

from datetime import date, datetime, timedelta

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT

class MaintenanceRequest(models.Model):
    _name = 'maintenance.request'
    _description = 'Maintenance Request'
    _inherit = ['mail.thread.cc', 'mail.activity.mixin']
    _order = 'sequence, id'
    _check_company_auto = True

    name = fields.Char(string="Request Name", required=True)
    equipment_id = fields.Many2one('maintenance.equipment', string="Equipment", ondelete="cascade")
    maintenance_team_id = fields.Many2one('maintenance.team', string="Maintenance Team", ondelete="set null")
    request_date = fields.Date(string="Request Date", default=fields.Date.today)
    close_date = fields.Date(string="Close Date")
    stage_id = fields.Many2one('maintenance.stage', string="Stage", ondelete="set null")
    category_id = fields.Many2one('maintenance.category', string="Category", ondelete="cascade")
    alias_id = fields.Many2one(
        'mail.alias', 'Alias', ondelete='restrict', required=True,
        help="Email alias for this equipment category. New emails will automatically "
        "create a new equipment under this category.")
    device_ids = fields.One2many('stock.move', 'order_id')
    user_id = fields.Many2one('res.users', string='Technician', tracking=True)
    owner_user_id = fields.Many2one('res.users', string='Created by User', default=lambda s: s.env.uid)
    employee_id = fields.Many2one('hr.employee', string="Employee")


    stock_status = fields.Selection([
        ('available', 'Available in Stock'),
        ('not_available', 'Not Available in Stock')
    ], string="Stock Status", compute="_compute_stock_status", store=True)

    @api.depends('equipment_id')
    def _compute_stock_status(self):
        for record in self:
            product_id = record.equipment_id.product_id.id if record.equipment_id and record.equipment_id.product_id else False
            if product_id:
                stock_quant = self.env['stock.quant'].search([
                    ('product_id', '=', product_id),
                    ('quantity', '>', 0)
                ], limit=1)
                record.stock_status = 'available' if stock_quant else 'not_available'
            else:
                record.stock_status = 'not_available'

    def _track_subtype(self, init_values):
        self.ensure_one()
        print("init_values:", init_values)  # Kiểm tra giá trị truyền vào
        if 'owner_user_id' in init_values and self.owner_user_id:
            return self.env.ref('maintenance.mt_mat_assign', raise_if_not_found=False)
        return super()._track_subtype(init_values)

    def action_validate_request(self):
        """Hàm xử lý chấp nhận hoặc hủy đơn bảo trì dựa trên tình trạng kho"""
        confirmed_stage = self.env.ref('maintenance.stage_confirmed', raise_if_not_found=False)
        cancelled_stage = self.env.ref('maintenance.stage_cancelled', raise_if_not_found=False)

        for record in self:
            if confirmed_stage and cancelled_stage:
                record.stage_id = confirmed_stage.id if record.stock_status == 'available' else cancelled_stage.id
