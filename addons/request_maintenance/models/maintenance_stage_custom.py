from odoo import models, fields

class MaintenanceStageCustom(models.Model):
    _name = "maintenance.stage.custom"
    _description = "Maintenance Stage Custom"
    
    name = fields.Char(string="Stage Name", required=True)
    sequence = fields.Integer(string="Sequence", default=10)
    legend_normal = fields.Char(string="Kanban Tooltip", default="Request is in progress")
    legend_done = fields.Char(string="Done Tooltip", default="Request is done")
    employee_id = fields.Many2one('hr.employee', string="Employee")
    done = fields.Boolean(string="Stage Done", default=False)
