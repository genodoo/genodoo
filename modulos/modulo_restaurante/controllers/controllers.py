# -*- coding: utf-8 -*-
from odoo import http, models, fields
from datetime import datetime, timedelta


class RestaurantController(http.Controller):
    @http.route('/reservas/submit', type='http', auth='public',
                methods=['POST'], website=True)
    def MakeReservation(self, **kw):
        date_str = "-".join([
            kw['day'],
            kw['hour']])
        date_obj = (datetime.strptime(date_str, "%Y-%m-%d-%H:%M") -
                    timedelta(hours=2))
        # date_str = fields.Datetime.to_string(date_obj)
        # print("date_str2=" + date_str)
        http.request.env['restaurant.reservation'].create({
            'client_name': kw['client_name'],
            'client_email': kw['client_email'],
            'day': date_obj,
            'phone_number': kw['phone_number'],
            'diners': kw['number_diners']
        })

        return http.request.render('modulo_restaurante.thanks')
