# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Pelicula(models.Model):

    _name = 'modulo_cine.pelicula'

    nombre = fields.Char(string='Nombre de la Pelicula', required=True)
    espectadores = fields.Integer(string='Visualizaciones totales', required=True)
    duracion = fields.Integer(string='Duracion en minutos', required=True)
    link = fields.Char(string='IMDB', required=True)

    _sql_constraints = [
        ('PK2',
         'UNIQUE(nombre)',
         "El nombre de la pelicula no se puede repetir"),
    ]
