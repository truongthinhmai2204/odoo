from odoo import models, fields

class StockMove(models.Model):
    _inherit = 'stock.move'

    maintenance_request_id = fields.Many2one('maintenance.request.custom', string='Maintenance Request')
    maintenance_team_id = fields.Many2one('maintenance.team', string="Maintenance Team")
    user_id = fields.Many2one('res.users', string='Technician', tracking=True)
    owner_user_id = fields.Many2one('res.users', string='Created by User', default=lambda s: s.env.uid)
    employee_id = fields.Many2one('hr.employee', string="Employee")
    category_id = fields.Many2one('maintenance.equipment.category', string="Equipment Category", ondelete="cascade")
    product_id = fields.Many2one('product.product', string='Related Product')