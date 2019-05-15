# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Reproducciones(models.Model):

    _name = 'cine.reproducciones'

    datetime = fields.Datetime(string='Fecha', required=True)
    pelicula_id = fields.Many2one(comodel_name='cine.pelicula', string='Película', required=True)
    sala_id = fields.Many2one(comodel_name='cine.sala', string='Sala', required=True)
    price = fields.Float(string='Precio', required=True)

    _sql_constraints = [
        ('PK4',
         'UNIQUE(nombre, numero_sala, fecha)',
         "La reproduccion no puede ser la misma"),
        ]

    @api.model
    def create(self, values):
        data = {
            'image': self.pelicula_id.image,
            'display_name': str(self.pelicula_id.name) + ' ' + str(self.datetime),
            'list_price': self.price
        }
        self.env["product.template"].create(data)
        return super(Reproducciones, self).create(values)
