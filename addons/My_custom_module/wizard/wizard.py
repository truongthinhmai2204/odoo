from odoo import models, fields, api

class YourWizard(models.TransientModel):
    _name = 'your.wizard'
    _description = 'Your Wizard'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')

    def action_confirm(self):
        # Add your logic here
        return {'type': 'ir.actions.act_window_close'}
