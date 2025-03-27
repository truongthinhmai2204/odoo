from odoo import http
from odoo.http import request

class MaintenanceRequestController(http.Controller):

    @http.route('/maintenance/requests', type='json', auth='user')
    def get_maintenance_requests(self):
        """API lấy danh sách yêu cầu bảo trì"""
        requests = request.env['maintenance.request'].sudo().search([])
        data = []
        for req in requests:
            data.append({
                'name': req.name,
                'equipment': req.equipment_id.name if req.equipment_id else 'N/A',
                'status': req.stage_id.name if req.stage_id else 'N/A',
                'owner': req.owner_user_id.name if req.owner_user_id else 'N/A',
            })
        return {'status': 'success', 'data': data}
