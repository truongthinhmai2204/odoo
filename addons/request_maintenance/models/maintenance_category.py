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
    user_id = fields.Many2one('res.users', string='Owner', tracking=True)
    owner_user_id = fields.Many2one('res.users', string='Created by User', default=lambda s: s.env.uid)
    employee_id = fields.Many2one('hr.employee', string="Employee")
    category_id = fields.Many2one('maintenance.category', string="Category", ondelete="cascade")
    order_id = fields.Many2one('sale.order', string="Order", ondelete="cascade", required=True)

