# -*- coding: utf-8 -*-
from odoo import http

class PeliculasCine(http.Controller):

    @http.route('/', type='http', auth='public', methods={'GET'}, website=True)
    def cinema_page(self, **kw):
        return http.request.render('modulo_cine.Home', {
            'films': http.request.env['cine.pelicula'].search([])
        })
        