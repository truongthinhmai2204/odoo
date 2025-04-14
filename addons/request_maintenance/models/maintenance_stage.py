from odoo import models, fields

class MaintenanceStage(models.Model):
    _name = "maintenance.stage"
    _description = "Maintenance Stage"
    
    name = fields.Char(string="Stage Name", required=True)
    sequence = fields.Integer(string="Sequence", default=10)
    user_id = fields.Many2one('res.users', string='Technician', tracking=True)
    owner_user_id = fields.Many2one('res.users', string='Created by User', default=lambda s: s.env.uid)
    device_ids = fields.One2many('stock.move', 'maintenance_request_id', string="Devices")
    employee_id = fields.Many2one('hr.employee', string="Employee")
    maintenance_request_id = fields.Many2one('maintenance.request', string="Maintenance Request")
    product_id = fields.Many2one('product.product', string='Related Product')
    legend_normal = fields.Char(string="Kanban Tooltip", default="Default text")
    legend_done = fields.Char(string="Done Tooltip", default="Completed")


