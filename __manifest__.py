# -*- coding: utf-8 -*-
{
    'name': "Odoo Object Direct Routes",

    'summary': """
        Allows you to use direct object routes.""",
    'version': '1.1',

    'description': """
        Using Direct Object Routes
    """,

    'author': "Diogo Duarte",
    'website': "http://diogocduarte.github.io/",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'crm'],
    'auto_install': True,
    'external_dependencies': {
        'python': [],
    },
    'data': [
        'views/actions_views.xml'
    ],
    'installable': True
}