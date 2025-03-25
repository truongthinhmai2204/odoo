from odoo import models, fields, api
import logging
from odoo.exceptions import ValidationError

class MaintenanceRequest(models.Model):
    _name = "maintenance.request"
    _description = "Maintenance Request"
    _inherit = 'maintenance.request'
    _logger = logging.getLogger(__name__)

    name = fields.Char(string="Request Name", required=True)
    equipment_id = fields.Many2one('maintenance.equipment', string="Equipment", ondelete="cascade")
    maintenance_team_id = fields.Many2one('maintenance.team', string="Maintenance Team", ondelete="set null")
    sale_order_id = fields.Many2one('sale.order', string="Đơn hàng liên kết")
    request_date = fields.Date(string="Request Date", default=fields.Date.today)
    close_date = fields.Date(string="Close Date")
    stage_id = fields.Many2one('maintenance.stage', string="Stage", ondelete="set null")
    category_id = fields.Many2one('maintenance.category', string="Category",ondelete="cascade")
    owner_user_id = fields.Many2one('res.users', string='Created by User', default=lambda self: self.env.uid, store=True)
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('rejected', 'Rejected'),
    ], default='draft', string="Status", tracking=True)

    def _test_log(self):
        self.__class__._logger.info(f"DEBUG: {self.env['res.users']._fields}")

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        for record in records:
            if record.equipment_id and not self._check_equipment_stock(record.equipment_id):
                record.write({'state': 'cancelled'})
                raise ValidationError(("Equipment does not exist, sales order will be cancelled"))
            record.write({'state': 'confirmed'})
        return records

    def _check_equipment_stock(self, equipment):
        stock_quant = self.env['stock.quant'].search([('product_id', '=', equipment.id), ('quantity', '>', 0)])
        return bool(stock_quant)
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'owner_user_id' not in vals:
                vals['owner_user_id'] = self.env.user.id  
        return super().create(vals_list)
