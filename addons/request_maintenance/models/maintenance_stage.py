from odoo import models, fields

class MaintenanceStage(models.Model):
    _name = "maintenance.stage"
    _description = "Maintenance Stage"
    
    name = fields.Char(string="Stage Name", required=True)
    sequence = fields.Integer(string="Sequence", default=10)
    legend_normal = fields.Char(string="Kanban Tooltip", default="Request is in progress")
    legend_done = fields.Char(string="Done Tooltip", default="Request is done")
    employee_id = fields.Many2one('hr.employee', string="Employee")
