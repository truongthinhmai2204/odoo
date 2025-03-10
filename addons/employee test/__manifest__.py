{
    'name': 'Employee & Contract Management',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Manage employees and their contracts',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_views.xml',
        'views/contract_views.xml',
    ],
    'installable': True,
    'application': True,
}
