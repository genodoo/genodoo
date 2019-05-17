# -*- coding: utf-8 -*-
{
    'name': "modulo_genodoo_tienda",

    'summary': """Gestion de la venta de los modulos de Genodoo""",

    'description': """
        Modulo dedicado a la gestion de la venta de los modulos de Genodoo
    """,

    'author': "The GenOdoo Team",
    'website': "github.com/genodoo",

    'category': 'Diseño' 'Comercio',
    'version': '1.0',

    'depends': ['base', 'website'],

    # always loaded
    'data': [
	'templates/template_gestion.xml',
	#'templates/template_formulario.xml',
	'templates/template_cine.xml',
	'templates/template_hotel.xml',
	'templates/template_personalizado.xml',
	'templates/template_restaurante.xml',
	'templates/template_tienda.xml',
    #'templates/view_formulario.xml',
    ],
}
