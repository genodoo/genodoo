# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Reservation(models.Model):
    _name = 'restaurant.reservation'

    client_name = fields.Char()
    client_email = fields.Char()
    phone_number = fields.Integer()
    day = fields.Datetime()
    diners = fields.Integer()
