from odoo import http
from odoo.http import request

class MyController(http.Controller):

    @http.route('/my_module/hello', auth='public', type='http', website=True)
    def hello_world(self):
        return "Hello, Odoo!"

    @http.route('/my_module/data', auth='public', type='json')
    def get_data(self):
        records = request.env['my.model'].sudo().search([])
        data = [{"id": rec.id, "name": rec.name} for rec in records]
        return data

    @http.route('/my_module/create', auth='user', type='json', methods=['POST'])
    def create_record(self, **kwargs):
        if 'name' in kwargs:
            new_record = request.env['my.model'].sudo().create({'name': kwargs['name']})
            return {"success": True, "id": new_record.id}
        return {"success": False, "error": "Missing name"}
