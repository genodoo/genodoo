# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website_form.controllers.main import WebsiteForm
from odoo.exceptions import ValidationError
import json
import logging

_logger = logging.getLogger(__name__)

class WebsiteForm(WebsiteForm):

    @http.route('/website_form/book', type="http", auth="public", methods=["POST"], website=True)
    def book_form(self, **kw):
        _logger.info("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        _logger.info(kw)
        book_id = request.env["hotel.book"].create(kw)
        return json.dumps({'id': book_id.id})

class BookPage(http.Controller):

    @http.route('/book', type="http", auth="public", methods=["GET"], website=True)
    def book_page(self, **kw):
        rooms = request.env["hotel.room"].search([])
        return request.render('gen_odoo_hotel.book_page_template', {
            'rooms': rooms
        })