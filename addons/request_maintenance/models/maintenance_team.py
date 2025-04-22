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

    todo_request_ids = fields.One2many('maintenance.request', string="Requests", copy=False, compute='_compute_todo_requests')
    todo_request_count = fields.Integer(string="Number of Requests", compute='_compute_todo_requests')
    todo_request_count_date = fields.Integer(string="Number of Requests Scheduled", compute='_compute_todo_requests')
    todo_request_count_high_priority = fields.Integer(string="Number of Requests in High Priority", compute='_compute_todo_requests')
    todo_request_count_block = fields.Integer(string="Number of Requests Blocked", compute='_compute_todo_requests')
    todo_request_count_unscheduled = fields.Integer(string="Number of Requests Unscheduled", compute='_compute_todo_requests')

    @api.depends('request_ids.stage_id.done')
    def _compute_todo_requests(self):
        for team in self:
            team.todo_request_ids = self.env['maintenance.request'].search([('maintenance_team_id', '=', team.id), ('stage_id.done', '=', False)])
            team.todo_request_count = len(team.todo_request_ids)
            team.todo_request_count_date = self.env['maintenance.request'].search_count([('maintenance_team_id', '=', team.id), ('schedule_date', '!=', False)])
            team.todo_request_count_high_priority = self.env['maintenance.request'].search_count([('maintenance_team_id', '=', team.id), ('priority', '=', '3')])
            team.todo_request_count_block = self.env['maintenance.request'].search_count([('maintenance_team_id', '=', team.id), ('kanban_state', '=', 'blocked')])
            team.todo_request_count_unscheduled = self.env['maintenance.request'].search_count([('maintenance_team_id', '=', team.id), ('schedule_date', '=', False)])

    @api.depends('equipment_ids')
    def _compute_equipment(self):
        for team in self:
            team.equipment_count = len(team.equipment_ids)

