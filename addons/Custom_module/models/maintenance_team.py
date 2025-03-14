from odoo import models, fields

class MaintenanceTeam(models.Model):
    _name = "maintenance.team"
    _description = "Maintenance Team"

    name = fields.Char(string="Team Name", required=True)
    request_ids = fields.One2many('maintenance.request', 'maintenance_team_id', string="Requests")
