{
    'name': 'Request Maintenance',
    'version': '1.0',
    'summary': 'Module quản lý yêu cầu bảo trì',
    'sequence': 10,
    'description': """Quản lý yêu cầu bảo trì và kiểm duyệt thiết bị""",
    'category': 'Maintenance',
    'website': 'https://yourcompany.com',
    'depends': ['maintenance'], 
    'data': [
        'security/ir.model.access.csv',           
        'data/maintenance_request_data.xml',      
        'data/maintenance_stage.xml',
        'data/data.xml',
        'views/maintenance_request.xml', 
        'views/maintenance_category.xml',
        'wizards/maintenance_wizard_view.xml',   
    ],
    'application': True,
    'installable': True,
    'auto_install': True,
    'assets': {
        'web.assets_backend': [
            'static/description/index.html',
        ],
    },
}
