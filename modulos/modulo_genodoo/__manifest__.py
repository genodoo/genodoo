# -*- coding: utf-8 -*-
{
    'name': "GenOdoo",

    'summary': """
       Web de GenOdoo""",

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
    'depends': ['base', 'website', 'website_form'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/home.xml',
        'views/newpage.xml',
        'templates/template_gestion.xml',
        'templates/template_formulario.xml',
        'templates/template_cine.xml',
        'templates/template_hotel.xml',
        'templates/template_personalizado.xml',
        'templates/template_restaurante.xml',
        'templates/template_tienda.xml',
        'templates/view_formulario.xml',
        'data/website_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True,
}
