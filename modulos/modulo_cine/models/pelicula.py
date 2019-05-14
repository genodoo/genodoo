# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Pelicula(models.Model):

    _name = 'cine.pelicula'

    name = fields.Char(string='Nombre', required=True)
    image = fields.Binary(string='Cartel')
    total_views = fields.Integer(string='Visualizaciones', readonly=True)
    duration = fields.Integer(string='Duración (Minutos)', required=True)
    link = fields.Char(string='Más Información', required=True)

    _sql_constraints = [
        ('PK2',
         'UNIQUE(name)',
         "El nombre de la pelicula no se puede repetir"),
    ]
