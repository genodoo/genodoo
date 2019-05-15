# -*- coding: utf-8 -*-
{
    'name': "GenOdoo Tienda",

    'summary': """
       Módulo para administrar tu tienda""",

    'description': """
       Administra tu tienda con este módulo, que incluye todo lo que necesitas para tu negocio, hasta el Sitio Web.
    """,

    'author': "rexuswolf",
    'website': "github.com/rexuswolf",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Comercio',
    'version': '1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'depends': ['website'],
    'depends': ['website_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/home.xml',
        'views/tienda.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
