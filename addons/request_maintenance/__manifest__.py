{
    'name': 'Request Maintenance',
    'version': '1.0',
    'summary': 'Module quản lý yêu cầu bảo trì',
    'sequence': 100,
    'description': """Quản lý yêu cầu bảo trì và kiểm duyệt thiết bị""",
    'category': 'Manufacturing/Maintenance',
    'website': 'https://yourcompany.com',
    'depends': ['mail', 'maintenance'], 
    'data': [
        'security/ir.rule.xml',         
        'security/ir.model.access.csv',  
        'views/maintenance_request.xml', 
        'views/maintenance_category.xml',
        'data/maintenance_request_data.xml',      
        'data/maintenance_stage.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'assets': {
        'web.assets_backend': [
            'static/description/index.html',
        ],
    },
    'license': 'LGPL-3',
}
