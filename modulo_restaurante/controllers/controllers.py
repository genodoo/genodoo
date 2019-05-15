# -*- coding: utf-8 -*-
from odoo import http, models, fields
from datetime import datetime


class RestaurantController(http.Controller):
    @http.route('/reservas/submit', type='http', auth='public', methods=['POST'], website=True)
    def make_reservation(self, **kw):
        month_translate = {'Enero':'01', 'Febrero':'02', 'Marzo':'03', 
        'Abril':'04', 'Mayo':'05', 'Junio':'06', 'Julio':'07', 'Agosto':'08', 
        'Septiembre':'09', 'Octubre':'10', 'Noviembre':'11', 'Diciembre':'12'}
        date_str = ",".join([
            str(kw['day']), 
            month_translate[kw['month']], 
            str(datetime.today().year),
            kw['hour']])
        date_obj = datetime.strptime(date_str, "%d,%m,%Y,%H:%M")
        date_str = fields.Datetime.to_string(date_obj)
        http.request.env['restaurant.reservation'].create({
            'client_name':kw['client_name'],
            'client_email':kw['client_email'],
            'day':date_str,
            'phone_number':kw['phone_number'],
            'diners':kw['number_diners']
        })
        
        return http.request.render('modulo_restaurante.thanks', lazy=False)
