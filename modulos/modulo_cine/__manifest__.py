# -*- coding: utf-8 -*-
{
    'name': "Genodoo Cinema",

    'summary': """Gestion de empresas de cine""",

    'description': """
        Modulo dedicado a la gestion de empresas de cine
    """,

    'author': "Genodoo",
    'website': "https://www.genodoo.com",

    'category': 'Sales, Specific Industry Applications, Website',
    'version': '1.0',

    'depends': [
        'base',
        'sale_management',
        'website',
        'point_of_sale'
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/template.xml',
        'views/bono.xml',
        'views/thanks.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True,
}
