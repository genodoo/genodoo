# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Reservation(models.Model):
    _name = 'restaurant.reservation'

    name = fields.Char()
    email = fields.Char()
    phone = fields.Integer()
    date = fields.Datetime()
    diners = fields.Integer()

    @api.multi
    def make(name_, email_, phone_, date_, diners_):
        return(self.create({
            'name':name_,
            'email':email_,
            'phone':phone_,
            'date':date_,
            'diners':diners_
        }))