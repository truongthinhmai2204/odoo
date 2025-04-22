from odoo import models, fields

class MaintenanceEquipmentCategory(models.Model):
    _name = "maintenance.equipment.category"
    _inherit = ['mail.alias.mixin', 'mail.thread']
    _description = "Maintenance Category"
    _rec_name = "name"

    name = fields.Char(string="Category Name", required=True)
    request_ids = fields.One2many('maintenance.request', 'category_id', string="Requests")
    technician_user_id = fields.Many2one('res.users', string='Responsible', tracking=True, default=lambda self: self.env.uid)
    owner_user_id = fields.Many2one('res.users', string='Created by User', default=lambda s: s.env.uid)
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company, index=True)
    device_ids = fields.One2many('stock.move', 'maintenance_request_id', string="Devices")
    employee_id = fields.Many2one('hr.employee', string="Employee")
    maintenance_request_id = fields.Many2one('maintenance.request', string="Main Maintenance Request")
    product_id = fields.Many2one('product.product', string='Related Product')
