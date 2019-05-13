# -*- coding: utf-8 -*-

from odoo import models, fields, api

 class reservation(models.Model):
    _name = 'restaurant.reservation'

    name = fields.Char()
    email = fields.Char()
    phone = fields.Integer()
    date = fields.Datetime()
    diners = fields.Integer()