from odoo import http
from odoo.http import request

class MaintenanceRequestController(http.Controller):

    @http.route('/maintenance/requests', type='json', auth='user')
    def get_maintenance_requests(self, limit=50):
        """API lấy danh sách yêu cầu bảo trì với giới hạn số lượng"""
        requests = request.env['maintenance.request'].sudo().search([], limit=limit)
        
        data = requests.read(['name', 'equipment_id', 'stage_id', 'owner_user_id'])
        
        for req in data:
            req['equipment'] = req.pop('equipment_id', False) and request.env['maintenance.equipment'].browse(req['equipment']).name or 'N/A'
            req['status'] = req.pop('stage_id', False) and request.env['maintenance.stage'].browse(req['status']).name or 'N/A'
            req['owner'] = req.pop('owner_user_id', False) and request.env['res.users'].browse(req['owner']).name or 'N/A'
        
        return {'status': 'success', 'data': data}
