from odoo import models, fields

class StockMove(models.Model):
    _inherit = 'stock.move'

    maintenance_request_id = fields.Many2one('maintenance.request', string='Maintenance Request')
    user_id = fields.Many2one('res.users', string='Technician', tracking=True)
    owner_user_id = fields.Many2one('res.users', string='Created by User', default=lambda s: s.env.uid)
    device_ids = fields.One2many('stock.move', 'maintenance_request_id', string="Devices")
    employee_id = fields.Many2one('hr.employee', string="Employee")
    category_id = fields.Many2one('maintenance.category', string="Category", ondelete="set null")
    product_id = fields.Many2one('product.product', string='Related Product')
