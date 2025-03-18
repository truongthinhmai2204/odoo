from odoo import models, fields

class MaintenanceCategory(models.Model):
    _name = "maintenance.category"
    _description = "Maintenance Category"

    name = fields.Char(string="Category Name", required=True)
    request_ids = fields.One2many(
        'maintenance.request',  
        'category_id',  
        string="Requests"
    )
