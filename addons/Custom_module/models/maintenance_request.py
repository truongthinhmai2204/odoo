from odoo import models, fields, api

class MaintenanceRequest(models.Model):
    _name = "maintenance.request"
    _description = "Maintenance Request"

    name = fields.Char(string="Request Name", required=True)
    category_id = fields.Many2one('maintenance.category', string="Category", ondelete="cascade")
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('rejected', 'Rejected'),
    ], default='draft', string="Status", tracking=True)

    def action_confirm_request(self):
        self.write({'state': 'confirmed'})

    def action_reject_request(self):
        self.write({'state': 'rejected'})
