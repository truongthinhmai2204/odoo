{
    'name': 'Equipment Confirmation',
    'version': '1.0',
    'summary': 'Module to confirm equipment',
    'description': 'A simple module to confirm equipment',
    'category': 'Tools',
    'author': 'Thinh',
    'depends': ['base', 'maintenance'],
    'data': [                       
        'views/equipment_confirmation.xml',
        'data/equipment_data.xml',
        'report/equipment_report.xml',
        'report/equipment_report_template.xml',
        'wizards/equipment_wizard_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,

    'assets': {
    'web.assets_backend': [
        'static/css/custom_style.css',
        'static/js/custom_script.js',
    ],
    },
}

