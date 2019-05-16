# -*- coding: utf-8 -*-
{
    'name': "modulo_cine",

    'summary': """Gestion de empresas de cine""",

    'description': """
        Modulo dedicado a la gestion de empresas de cine
    """,

    'author': "Genodoo",
    'website': "https://www.genodoo.com",

    'category': 'Sales, Specific Industry Applications, Website',
    'version': '0.1',

    'depends': ['base', 'sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True,
}
