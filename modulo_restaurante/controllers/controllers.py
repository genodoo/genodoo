# -*- coding: utf-8 -*-
from odoo import http

class RestaurantController(http.Controller):
    @http.route('/reservas/submit', type='http', auth='public', methods=['POST'])
    def make_reservation(self, **kw):
            response = http.HttpRequest.render('../views/thanks.xml', {})
            print(response)
            return response
