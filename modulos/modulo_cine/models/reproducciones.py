 # -*- coding: utf-8 -*-

from odoo import models, fields, api


class Reproducciones(models.Model):

    _name = 'cine.reproducciones'

    datetime = fields.Datetime(string='Fecha', required=True)
    pelicula_id = fields.Many2one(comodel_name='cine.pelicula', string='Película', required=True)
    sala_id = fields.Many2one(comodel_name='cine.sala', string='Sala', required=True)
    price = fields.Float(string='Precio', required=True, default=5.49)

    _sql_constraints = [
        ('PK4',
         'UNIQUE(nombre, numero_sala, fecha)',
         "La reproduccion no puede ser la misma"),
        ]

    @api.model
    def create(self, values):
        pelicula = self.env['cine.pelicula'].search([("id", "=", values['pelicula_id'])])
        data = {
            'name': str(pelicula.name) + ' ' + str(values['datetime']),
            'image': pelicula.image,
            'sale_ok': True,
            'purchase_ok': False,
            'type': "consu",
            'categ_id': 1,
            'list_price': values['price'],
            'standard_price': values['price']
        }
        self.env["product.template"].create(data)
        return super(Reproducciones, self).create(values)
