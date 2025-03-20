from odoo import models, fields, api

class MaintenanceRequest(models.Model):
    _name = "maintenance.request"
    _description = "Maintenance Request"
    _inherit = 'maintenance.request'

    name = fields.Char(string="Request Name", required=True)
    equipment_id = fields.Many2one('maintenance.equipment', string="Equipment", ondelete="cascade")
    maintenance_team_id = fields.Many2one('maintenance.team', string="Maintenance Team", ondelete="set null")
    request_date = fields.Date(string="Request Date", default=fields.Date.today)
    close_date = fields.Date(string="Close Date")
    stage_id = fields.Many2one(
        'maintenance.stage', 
        string="Stage", 
        ondelete="set null"
    )

    owner_user_id = fields.Many2one('res.users', string="Owner User", store=True)

    category_id = fields.Many2one(
        'maintenance.category', 
        string="Category",
        ondelete="cascade"
    )
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('rejected', 'Rejected'),
    ], default='draft', string="Status", tracking=True)

    def action_confirm_request(self):
        self.write({'state': 'confirmed'})

    def action_reject_request(self):
        self.write({'state': 'rejected'})
