from odoo import models, fields

class MaintenanceTeam(models.Model):
    _name = "maintenance.team"
    _description = "Maintenance Team"

    name = fields.Char(string="Team Name", required=True)
    request_ids = fields.One2many('maintenance.request', 'maintenance_team_id', string="Requests")
    user_id = fields.Many2one('res.users', string='Owner', tracking=True)
    owner_user_id = fields.Many2one('res.users', string='Created by User', default=lambda s: s.env.uid)
    employee_id = fields.Many2one('hr.employee', string="Employee")
    category_id = fields.Many2one('maintenance.category', string="Category", ondelete="cascade")
    order_id = fields.Many2one('sale.order', string="Order")

