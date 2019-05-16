# -*- coding: utf-8 -*-
{
    'name': "GenOdoo Hotel",

    'summary': """
       Módulo para administrar un hotel""",

    'description': """
       Este módulo te instalará las funcionalidades básicas para administrar tu hotel, así como el sitio web y el formulario de reservas.
    """,

    'author': "The GenOdoo Team",
    'website': "github.com/genodoo",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Comercio',
    'version': '1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'depends': ['website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/home.xml',
        'views/reservas.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True,
}
