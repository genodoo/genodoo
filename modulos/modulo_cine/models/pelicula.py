# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Pelicula(models.Model):

    _name = 'cine.pelicula'

    name = fields.Char(string='Film Name', required=True)
    totalViews = fields.Integer(string='Total Views', required=True)
    duration = fields.Integer(string='Duration (Minutes)', required=True)
    link = fields.Char(string='Info - Link', required=True)

    _sql_constraints = [
        ('PK2',
         'UNIQUE(nombre)',
         "El nombre de la pelicula no se puede repetir"),
    ]
