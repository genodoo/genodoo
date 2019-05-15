# -*- coding: utf-8 -*-
from odoo import http

class PeliculasCine(http.Controller):

    @http.route('/modulo_cine', type='http', auth='public', methods={'GET'}, website=True)
    def list(self, **kw):
        return http.request.render('modulo_cine.listing', {
            'films': http.request.env['cine.pelicula'].search([]),
        })
        