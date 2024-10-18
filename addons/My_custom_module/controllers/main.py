from odoo import http

class YourModuleName(http.Controller):
    @http.route('/your_module_name/', auth='public', website=True)
    def index(self, **kw):
        return "Hello, world!"

    @http.route('/your_module_name/objects/', auth='public', website=True)
    def list(self, **kw):
        return http.request.render('your_module_name.listing', {
            'root': '/your_module_name/objects',
            'objects': http.request.env['your_module_name.model'].search([]),
        })

    @http.route('/your_module_name/objects/<model("your_module_name.model"):obj>/', auth='public', website=True)
    def object(self, obj, **kw):
        return http.request.render('your_module_name.object', {
            'object': obj
        })
