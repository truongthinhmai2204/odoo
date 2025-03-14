{
    'name': 'Maintenance Request Management',
    'version': '1.0',
    'summary': 'Module quản lý yêu cầu bảo trì',
    'sequence': 10,
    'description': """Quản lý yêu cầu bảo trì và kiểm duyệt thiết bị""",
    'category': 'Maintenance',
    'author': 'KenZ',
    'website': 'https://yourcompany.com',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],  
    'data': [
        'security/ir.model.access.csv',           
        'views/maintenance_request.xml', 
        'data/maintenance_data.xml',      
        'wizards/maintenance_wizard_views.xml',   
        'static/description/index.html',  
        'i18n/en.po',                     
    ],
    'assets': {
        'web.assets_backend': [
            'static/description/index.html',
        ],
    },
    'application': True,
    'installable': True,
    'auto_install': False,
}
