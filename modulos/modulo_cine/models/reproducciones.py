# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Reproducciones(models.Model):

    _name = 'cine.reproducciones'

    datetime = fields.Datetime(string='Fecha', required=True, index=True)
    pelicula_id = fields.Many2one(comodel_name='cine.pelicula', string='Película', ondelete='set null', required='true')
    sala_id = fields.Many2one(comodel_name='cine.sala', string='Sala', ondelete='set null', required='true')
    price = fields.Integer(string='Precio', required='true')

    _sql_constraints = [
        ('PK4',
         'UNIQUE(nombre, numero_sala, fecha)',
         "La reproduccion no puede ser la misma"),
        ]
