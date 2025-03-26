{
    'name': 'Maintenance Request Management',
    'version': '1.0',
    'summary': 'Module quản lý yêu cầu bảo trì',
    'sequence': 10,
    'description': """Quản lý yêu cầu bảo trì và kiểm duyệt thiết bị""",
    'category': 'Maintenance',
    'website': 'https://yourcompany.com',
    'depends': ['mail'], 
    'data': [
        'security/ir.model.access.csv',           
        'views/maintenance_request.xml', 
        'data/maintenance_data.xml',      
        'data/maintenance_stage.xml',
        'views/maintenance_category.xml',
        'views/maintenance_request.xml',
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
}
