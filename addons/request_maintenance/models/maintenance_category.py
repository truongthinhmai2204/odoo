from odoo import models, fields

class MaintenanceCategory(models.Model):
    _name = "maintenance.category"
    _description = "Maintenance Category"
    _order = 'sequence, id'

    name = fields.Char(string="Category Name", required=True)
    request_ids = fields.One2many(
        'maintenance.request',  
        'category_id',  
        string="Requests"
    )
    user_id = fields.Many2one('res.users', string='Technician', tracking=True)
    owner_user_id = fields.Many2one('res.users', string='Created by User', default=lambda s: s.env.uid)
    device_ids = fields.One2many('stock.move', 'maintenance_request_id', string="Devices")
    category_id = fields.Many2one('maintenance.category', string="Category", ondelete="cascade")
    employee_id = fields.Many2one('hr.employee', string="Employee")
    maintenance_request_id = fields.Many2one('maintenance.request', string="Maintenance Request")
    product_id = fields.Many2one('product.product', string='Related Product')

