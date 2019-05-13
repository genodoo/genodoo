# -*- coding: utf-8 -*-
from odoo import http

# class Viewtractor(http.Controller):
#     @http.route('/viewtractor/viewtractor/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/viewtractor/viewtractor/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('viewtractor.listing', {
#             'root': '/viewtractor/viewtractor',
#             'objects': http.request.env['viewtractor.viewtractor'].search([]),
#         })

#     @http.route('/viewtractor/viewtractor/objects/<model("viewtractor.viewtractor"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('viewtractor.object', {
#             'object': obj
#         })