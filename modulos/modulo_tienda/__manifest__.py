{
    'name': 'GenOdoo Shop',
    'category': 'Website',
    'sequence': 55,
    'summary': 'Sell Your Products Online',
    'author': 'The GenOdoo Team',
    'website': 'https://www.odoo.com/page/e-commerce',
    'version': '1.0',
    'description': "",
    'depends': [
        'website',
        'website_sale',
        'sale_payment',
        'website_payment',
        'website_mail',
        'website_form',
        'website_rating',
        'sale_management'
        'point_of_sale'
    ],
    'data': [
        'views/home.xml',
    ],
    'demo': [
        'data/demo.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}
