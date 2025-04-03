from odoo import models, fields

class MaintenanceEquipment(models.Model):
    _name = 'maintenance.equipment'
    _description = 'Maintenance Equipment'

    name = fields.Char(string="Equipment Name", required=True)
    description = fields.Text(string="Description")
    user_id = fields.Many2one('res.users', string='Owner', tracking=True)
    owner_user_id = fields.Many2one('res.users', string='Created by User', default=lambda s: s.env.uid)
