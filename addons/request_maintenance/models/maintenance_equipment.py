from odoo import models, fields

class MaintenanceEquipment(models.Model):
    _name = 'maintenance.equipment'
    _description = 'Maintenance Equipment'

    name = fields.Char(string="Equipment Name", required=True)
    description = fields.Text(string="Description")
