from odoo import models, fields

class MaintenanceStage(models.Model):
    _name = "maintenance.stage"
    _description = "Maintenance Stage"
    
    name = fields.Char(string="Stage Name", required=True)
    sequence = fields.Integer(string="Sequence", default=10)
    user_id = fields.Many2one('res.users', string='Technician', tracking=True)
    owner_user_id = fields.Many2one('res.users', string='Created by User', default=lambda s: s.env.uid)
    alias_id = fields.Many2one(
        'mail.alias', 'Alias', ondelete='restrict', required=True,
        help="Email alias for this equipment category. New emails will automatically "
        "create a new equipment under this category.")
    device_ids = fields.One2many('stock.move', 'maintenance_request_id', string="Devices")
    employee_id = fields.Many2one('hr.employee', string="Employee")
    category_id = fields.Many2one('maintenance.category', string="Category", ondelete="cascade")
    order_id = fields.Many2one('sale.order', string="Order")

