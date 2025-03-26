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
    owner_user_id = fields.Many2one('res.users', string='Created by User')   

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('rejected', 'Rejected'),
    ], default='draft', string="Status", tracking=True)

    def _test_log(self, vals_list):
        _logger.info("Vals before create: %s", vals_list)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'owner_user_id' not in vals:
                vals['owner_user_id'] = self.env.user.id
        self._test_log(vals_list)
        return super(MaintenanceRequest, self).create(vals_list)
        stock_quant = self.env['stock.quant'].search([('product_id', '=', equipment.id), ('quantity', '>', 0)], limit=1)
        return bool(stock_quant)
    
    @api.model_create_multi
        self._test_log(vals_list)
        return super().create(vals_list)
