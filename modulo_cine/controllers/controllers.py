# -*- coding: utf-8 -*-
from odoo import http

# class ModuloCine(http.Controller):
#     @http.route('/modulo_cine/modulo_cine/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_cine/modulo_cine/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_cine.listing', {
#             'root': '/modulo_cine/modulo_cine',
#             'objects': http.request.env['modulo_cine.modulo_cine'].search([]),
#         })

#     @http.route('/modulo_cine/modulo_cine/objects/<model("modulo_cine.modulo_cine"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_cine.object', {
#             'object': obj
#         })
