from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class MaintenanceRequest(models.Model):
    _name = "maintenance.request"
    _description = "Maintenance Request"
    _inherit = 'maintenance.request'

    name = fields.Char(string="Request Name", required=True)
    equipment_id = fields.Many2one('maintenance.equipment', string="Equipment", ondelete="cascade")
    maintenance_team_id = fields.Many2one('maintenance.team', string="Maintenance Team", ondelete="set null")
    sale_order_id = fields.Many2one('sale.order', string="Đơn hàng liên kết")
    request_date = fields.Date(string="Request Date", default=fields.Date.today)
    close_date = fields.Date(string="Close Date")
    stage_id = fields.Many2one('maintenance.stage', string="Stage", ondelete="set null")
    category_id = fields.Many2one('maintenance.category', string="Category",ondelete="cascade")
    user_id = fields.Many2one('res.users', string='Technician', tracking=True)
    owner_user_id = fields.Many2one('res.users', string='Created by User')   

    stock_status = fields.Selection([
        ('available', 'Available in Stock'),
        ('not_available', 'Not Available in Stock')
    ], string="Stock Status", compute="_compute_stock_status", store=True)

    @api.depends('equipment_id')
    def _compute_stock_status(self):
        for record in self:
            stock_quant = self.env['stock.quant'].search([
                ('product_id', '=', record.equipment_id.product_id.id),
                ('quantity', '>', 0)
            ], limit=1)
            record.stock_status = 'available' if stock_quant else 'not_available'

    def action_validate_request(self):
        """Hàm xử lý chấp nhận hoặc hủy đơn bảo trì dựa trên tình trạng kho"""
        for record in self:
            if record.stock_status == 'available':
                record.stage_id = self.env.ref('maintenance.stage_confirmed').id  # Chuyển trạng thái "Đã duyệt"
            else:
                record.stage_id = self.env.ref('maintenance.stage_cancelled').id