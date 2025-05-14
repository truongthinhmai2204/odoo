{
    'name': 'Break Timer Reminder',
    'version': '1.0',
    'summary': 'Nhắc nghỉ ngơi định kỳ và thống kê thời gian làm việc',
    'author': 'Thinh Mai',
    'category': 'Human Resources',
    'depends': ['base', 'web'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/break_config.xml',
        'views/break_config_views.xml',
        'views/break_session_views.xml',
        'views/timer_widget_test_view.xml',
    ],
    "assets": {
        'web.assets_backend': [
            'break_timer_reminder/static/src/js/timer_widget.js',
            'break_timer_reminder/static/src/xml/timer_widget.xml',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
