# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Reproducciones(models.Model):

    _name = 'modulo_cine.reproducciones'

    nombre = fields.One2many('modulo_cine.pelicula', 'nombre')
    numero_sala = fields.One2many('modulo_cine.sala', 'numero_sala')
    fecha = fields.Date(string='Fecha')
    precio = fields.Float(string='Precio', required=True)

    _sql_constraints = [
        ('PK4',
         'UNIQUE(nombre, numero_sala, fecha)',
         "La reproduccion no puede ser la misma"),
        ]
