{
    'name': 'Your Module Name',
    'summary': 'Module summary',
    'description': """
    Your module description
    """,
    'author': 'Your Name',
    'website': 'http://www.yourwebsite.com',
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
