from odoo import models, fields

class MaintenanceWizard(models.TransientModel):
    _name = 'maintenance.wizard'
    _description = 'Maintenance Approval Wizard'

    confirm = fields.Boolean(string="Xác nhận")

    def action_confirm(self):
        active_id = self.env.context.get('active_id')
        if active_id:
            request = self.env['maintenance.request'].browse(active_id)
            if self.confirm:
                request.state = 'approved'
            else:
                request.state = 'rejected'
