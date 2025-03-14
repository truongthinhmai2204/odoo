from odoo import models, fields

class MaintenanceStage(models.Model):
    _name = "maintenance.stage"
    _description = "Maintenance Stage"
    
    name = fields.Char(string="Stage Name", required=True)
    sequence = fields.Integer(string="Sequence", default=10)
