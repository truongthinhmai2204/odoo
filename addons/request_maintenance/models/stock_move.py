from odoo import models, fields

class StockMove(models.Model):
    _inherit = 'stock.move'

    maintenance_request_id = fields.Many2one('maintenance.request', string='Maintenance Request')
