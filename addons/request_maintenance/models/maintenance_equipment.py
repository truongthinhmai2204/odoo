from odoo import models, fields

class MaintenanceEquipment(models.Model):
    _name = 'maintenance.equipment'
    _description = 'Maintenance Equipment'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Equipment Name", required=True)
    description = fields.Text(string="Description")
    technician_user_id = fields.Many2one('res.users', string='Technician', tracking=True)   
    category_id = fields.Many2one('maintenance.equipment.category', string="Equipment Category", ondelete="set null") 
    owner_user_id = fields.Many2one('res.users', string='Created by User', default=lambda s: s.env.uid)
    device_ids = fields.One2many('stock.move', 'maintenance_request_id', string="Devices")
    employee_id = fields.Many2one('hr.employee', string="Employee")
    maintenance_request_id = fields.Many2one('maintenance.request', string="Maintenance Request")
    product_id = fields.Many2one('product.product', string='Related Product')



