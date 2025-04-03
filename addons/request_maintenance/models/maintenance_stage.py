from odoo import models, fields

class MaintenanceStage(models.Model):
    _name = "maintenance.stage"
    _description = "Maintenance Stage"
    
    name = fields.Char(string="Stage Name", required=True)
    sequence = fields.Integer(string="Sequence", default=10)
    user_id = fields.Many2one('res.users', string='Owner', tracking=True)
    owner_user_id = fields.Many2one('res.users', string='Created by User', default=lambda s: s.env.uid)
    employee_id = fields.Many2one('hr.employee', string="Employee")
    category_id = fields.Many2one('maintenance.category', string="Category", ondelete="cascade")
