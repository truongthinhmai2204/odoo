from odoo import models, fields

class MaintenanceEquipment(models.Model):
    _name = 'maintenance.equipment'
    _description = 'Maintenance Equipment'

    name = fields.Char(string="Equipment Name", required=True)
    description = fields.Text(string="Description")
    user_id = fields.Many2one('res.users', string='Technician', tracking=True)
    owner_user_id = fields.Many2one('res.users', string='Created by User', default=lambda s: s.env.uid)
    device_ids = fields.One2many('stock.move', 'maintenance_request_id', string="Devices")
    employee_id = fields.Many2one('hr.employee', string="Employee")
    category_id = fields.Many2one('maintenance.category', string="Category", ondelete="cascade")
    maintenance_request_id = fields.Many2one('maintenance.request', string="Maintenance Request")
    product_id = fields.Many2one('product.product', string='Related Product')



