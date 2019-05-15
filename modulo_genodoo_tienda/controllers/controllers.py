# -*- coding: utf-8 -*-
from odoo import http

class PageController(http.Controller):
    @http.route('/1_modulo_tienda', type='http', auth='public', methods=['GET'], website=True)
    def page_tienda(self, **kw):
        return http.request.render('modulo_genodoo_tienda.Modulo_GenOdoo_tienda')

class PageController(http.Controller):
    @http.route('/2_modulo_cine', type='http', auth='public', methods=['GET'], website=True)
    def page_cine(self, **kw):
        return http.request.render('modulo_genodoo_tienda.Modulo_GenOdoo_cine')

class PageController(http.Controller):
    @http.route('/3_modulo_hotel', type='http', auth='public', methods=['GET'], website=True)
    def page_hotel(self, **kw):
        return http.request.render('modulo_genodoo_tienda.Modulo_GenOdoo_hotel')

class PageController(http.Controller):
    @http.route('/4_modulo_restaurante', type='http', auth='public', methods=['GET'], website=True)
    def page_restaurante(self, **kw):
        return http.request.render('modulo_genodoo_tienda.Modulo_GenOdoo_restaurante')

class PageController(http.Controller):
    @http.route('/5_modulo_personalizado', type='http', auth='public', methods=['GET'], website=True)
    def page_personalizado(self, **kw):
        return http.request.render('modulo_genodoo_tienda.Modulo_GenOdoo_personalizado')

class PageController(http.Controller):
    @http.route('/shop', type='http', auth='public', methods=['GET'], website=True)
    def page_modulos(self, **kw):
        return http.request.render('modulo_genodoo_tienda.Modulos_GenOdoo')
