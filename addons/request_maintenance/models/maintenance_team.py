from odoo import models, fields
from odoo import api, fields, models, SUPERUSER_ID, _

class MaintenanceTeam(models.Model):
    _name = "maintenance.team"
    _description = "Maintenance Team"

    name = fields.Char(string="Team Name", required=True)
    request_ids = fields.One2many('maintenance.request', 'maintenance_team_id', string="Requests")
    user_id = fields.Many2one('res.users', string='Technician', tracking=True)
    color = fields.Integer("Color Index", default=0)
    active = fields.Boolean(string="Active", default=True)
    member_ids = fields.Many2many(
        'res.users', 'maintenance_team_users_rel', string="Team Members",
        domain="[('company_ids', 'in', company_id)]")
    owner_user_id = fields.Many2one('res.users', string='Created by User', default=lambda s: s.env.uid)
    employee_id = fields.Many2one('hr.employee', string="Employee")
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company, index=True)
