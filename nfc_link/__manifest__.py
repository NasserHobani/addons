# -*- coding: utf-8 -*-
{
    'name': "nfc_link",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "nasserdev",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website','contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/access_right.xml',
        # 'data/ir_actions_data.xml',
        'data/website_form.xml',
        'data/website_action.xml',
        'views/menu.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'auto_install': True,
    'assets': {
        'website.assets_editor': [
            'website_crm/static/src/**/*',
        ]
    },
}
