from odoo import http
from odoo.http import request

class MaintenanceController(http.Controller):
    @http.route('/maintenance/request', type='json', auth='user')
    def get_maintenance_requests(self):
        requests = request.env['maintenance.request'].search([])
        return [{'id': r.id, 'name': r.name, 'state': r.state} for r in requests]
