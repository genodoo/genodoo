# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website_form.controllers.main import WebsiteForm
import json

class Page1Controller(http.Controller):
    @http.route('/1_modulo_tienda', type='http', auth='public', methods=['GET'], website=True)
    def page_tienda(self, **kw):
        return http.request.render('modulo_genodoo.Modulo_GenOdoo_tienda')

class Page2Controller(http.Controller):
    @http.route('/2_modulo_cine', type='http', auth='public', methods=['GET'], website=True)
    def page_cine(self, **kw):
        return http.request.render('modulo_genodoo.Modulo_GenOdoo_cine')

class Page3Controller(http.Controller):
    @http.route('/3_modulo_hotel', type='http', auth='public', methods=['GET'], website=True)
    def page_hotel(self, **kw):
        return http.request.render('modulo_genodoo.Modulo_GenOdoo_hotel')

class Page4Controller(http.Controller):
    @http.route('/4_modulo_restaurante', type='http', auth='public', methods=['GET'], website=True)
    def page_restaurante(self, **kw):
        return http.request.render('modulo_genodoo.Modulo_GenOdoo_restaurante')

class Page5Controller(http.Controller):
    @http.route('/5_modulo_personalizado', type='http', auth='public', methods=['GET'], website=True)
    def page_personalizado(self, **kw):
        return http.request.render('modulo_genodoo.Modulo_GenOdoo_personalizado')

class Page6Controller(http.Controller):
    @http.route('/modulos', type='http', auth='public', methods=['GET'], website=True)
    def page_modulos(self, **kw):
        return http.request.render('modulo_genodoo.Modulos_GenOdoo')

class PedidosController(http.Controller):
    @http.route('/pedidos', type='http', auth='public', methods=['GET'], website=True)
    def page_pedidos(self, **kw):
       return request.render('modulo_genodoo.Pagina_pedidos')

class WebsiteForm(WebsiteForm):
    @http.route('/website_form/pedidos', type='http', auth='public', methods=['POST'], website=True)
    def form_pedidos(self, **kw):
       pedido_id = request.env["genodoo.pedido"].create(kw)
       return json.dumps({'id': pedido_id.id})


