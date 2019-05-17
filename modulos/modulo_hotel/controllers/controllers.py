# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website_form.controllers.main import WebsiteForm
from odoo.exceptions import ValidationError
import json
import logging

_logger = logging.getLogger(__name__)


class BookForm(WebsiteForm):

    @http.route('/website_form/book', type="http", auth="public", methods=["POST"], website=True)
    def book_form(self, **kw):
        ref = request.env["hotel.book"].search_count([]) + 1
        kw.update({'name': ref})
        if request.env['res.partner'].search_count([('name', '=', kw['customer_id'])]) == 0:
            request.env['res.partner'].create({'name': kw['customer_id']})
        kw['customer_id'] = request.env['res.partner'].search([('name', '=', kw['customer_id'])]).id
        book_id = request.env["hotel.book"].create(kw)
        return json.dumps({'id': book_id.id})


class BookPage(http.Controller):

    @http.route('/book', type="http", auth="public", methods=["GET"], website=True)
    def book_page(self, **kw):
        rooms = request.env["hotel.room"].search([])
        return request.render('modulo_hotel.book_page_template', {
            'rooms': rooms
        })
