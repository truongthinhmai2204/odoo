{
    'name': 'First Custom module Odoo',
    'summary': 'Module summary',
    'description': """
    Your module description
    """,
    'author': 'Mai Trường Thịnh',
    'website': 'http://www.believeme.com',
    'category': 'Category',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/library_book.xml'
        'security/ir.model.access.csv',
        'views/your_model_views.xml',
        'views/your_wizard_views.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
}
