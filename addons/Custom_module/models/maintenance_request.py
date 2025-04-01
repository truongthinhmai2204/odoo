from odoo import models, fields, api

class MaintenanceRequest(models.Model):
    _inherit = 'maintenance.request'

    name = fields.Char(string="Request Name", required=True)
    equipment_id = fields.Many2one('maintenance.equipment', string="Equipment", ondelete="cascade")
    maintenance_team_id = fields.Many2one('maintenance.team', string="Maintenance Team", ondelete="set null")
    sale_order_id = fields.Many2one('sale.order', string="Đơn hàng liên kết")
    request_date = fields.Date(string="Request Date", default=fields.Date.today)
    close_date = fields.Date(string="Close Date")
    stage_id = fields.Many2one('maintenance.stage', string="Stage", ondelete="set null")
    category_id = fields.Many2one('maintenance.category', string="Category", ondelete="cascade")
    user_id = fields.Many2one('res.users', string='Owner', tracking=True)
    owner_user_id = fields.Many2one('res.users', string='Created by User', ondelete="set null")

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

    def action_validate_request(self):
        """Hàm xử lý chấp nhận hoặc hủy đơn bảo trì dựa trên tình trạng kho"""
        confirmed_stage = self.env.ref('maintenance.stage_confirmed', raise_if_not_found=False)
        cancelled_stage = self.env.ref('maintenance.stage_cancelled', raise_if_not_found=False)
        
        for record in self:
            if confirmed_stage and cancelled_stage:
                record.stage_id = confirmed_stage.id if record.stock_status == 'available' else cancelled_stage.id
