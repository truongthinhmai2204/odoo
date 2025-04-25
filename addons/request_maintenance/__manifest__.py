{
    'name': 'Custom Maintenance Request',
    'version': '1.0',
    'summary': 'Module quản lý yêu cầu bảo trì',
    'sequence': 100,
    'description': """Quản lý yêu cầu bảo trì và kiểm duyệt thiết bị""",
    'category': 'Manufacturing/Maintenance',
    'website': 'https://yourcompany.com',
    'depends': ['maintenance', 'stock'], 
    'data': [
        'security/ir.rule.xml',         
        'security/ir.model.access.csv',  
        'data/maintenance_stage.xml',
        'views/maintenance_category.xml',
        'views/maintenance_request.xml', 
        'data/maintenance_request_data.xml',      
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
