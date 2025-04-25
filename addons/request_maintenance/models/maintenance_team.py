from odoo import models, fields
from odoo import api, fields, models, SUPERUSER_ID, _

class MaintenanceTeam(models.Model):
    _name = "maintenance.team"
    _description = "Maintenance Team"

    name = fields.Char(string="Team Name", required=True)
    equipment_ids = fields.One2many('maintenance.equipment', 'maintenance_team_id', copy=False)
    user_id = fields.Many2one('res.users', string='Technician', tracking=True)
    color = fields.Integer("Color Index", default=0)
    active = fields.Boolean(string="Active", default=True)
    member_ids = fields.Many2many(
        'res.users', 'maintenance_team_users_rel', string="Team Members",
        domain="[('company_ids', 'in', company_id)]")
    owner_user_id = fields.Many2one('res.users', string='Created by User', default=lambda s: s.env.uid)
    employee_id = fields.Many2one('hr.employee', string="Employee")
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company, index=True)
    request_ids = fields.One2many('maintenance.request', 'maintenance_team_id', copy=False)
    todo_request_ids = fields.One2many(
    'maintenance.request', 'maintenance_team_id',
    string="To-do Requests"
    )

    #dashboard
    @api.depends('request_ids.stage_id.done')
    def _compute_todo_requests(self):
        for team in self:
            team.todo_request_ids = self.env['maintenance.request'].search([('maintenance_team_id', '=', team.id), ('stage_id.done', '=', False)])
           
    @api.depends('equipment_ids')
    def _compute_equipment(self):
        for team in self:
            team.equipment_count = len(team.equipment_ids)
