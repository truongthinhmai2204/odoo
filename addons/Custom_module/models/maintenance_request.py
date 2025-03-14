from odoo import models, fields, api

class MaintenanceRequest(models.Model):
    _inherit = 'maintenance.request'

    state = fields.Selection([
        ('draft', 'Draft'),
        ('waiting_approval', 'Waiting Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('done', 'Done')
    ], default='draft', string="Status")

    warehouse_confirmed = fields.Boolean(string="Warehouse Confirmed", default=False)

    def action_confirm_warehouse(self):
        for record in self:
            if record.equipment_id and self.env['stock.quant'].search([
                ('product_id', '=', record.equipment_id.product_id.id),
                ('quantity', '>', 0)
            ]):
                record.warehouse_confirmed = True
                record.state = 'waiting_approval'
            else:
                record.state = 'rejected'

    def action_approve(self):
        for record in self:
            if record.state == 'waiting_approval':
                record.state = 'approved'

    def action_reject(self):
        for record in self:
            record.state = 'rejected'