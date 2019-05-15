# -*- coding: utf-8 -*-
{
    'name': "GenOdoo Tienda",

    'summary': """
       Importa tus estilos de páginas web mediante este módulo""",

    'description': """
       Mediante este módulo podemos importar templates como vistas en nuestro Sitio Web,
       consiguiendo así transportar nuestros diseños de páginas web creadas con la herramienta
       Drag & Drop que nos proporciona Odoo.
       Además, dispone de dos plantillas, una para modificar la página inicial del Sitio Web
       y otra para crear una nueva página con el estilo que queramos.
    """,

    'author': "rexuswolf",
    'website': "github.com/rexuswolf",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Comercio',
    'version': '1.0.1',

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
