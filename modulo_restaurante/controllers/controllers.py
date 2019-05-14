# -*- coding: utf-8 -*-
from odoo import http

class RestaurantController(http.Controller):
    @http.route('/reservas/submit', type='http', auth='public', methods=['GET', 'POST'], website=True)
    def make_reservation(self, **kw):
            response = http.request.render('modulo_restaurante.thanks', lazy=False)
            return response
