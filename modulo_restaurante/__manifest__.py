# -*- coding: utf-8 -*-
{
    'name': "GenOdoo Restaurant",

    'summary': """
       Módulo para manejar un restaurante""",

    'description': """
    """,

    'author': "The GenOdoo Team",
    'website': "github.com/genodoo",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Diseño',
    'version': '1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/reservas.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
