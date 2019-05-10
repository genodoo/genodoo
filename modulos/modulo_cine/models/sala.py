# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Sala(models.Model):

    _name = 'modulo_cine.sala'

    numero_sala = fields.Char(string='Numero de Sala', required=True)
    capacidad = fields.Integer(string='Capacidad', required=True)

    _sql_constraints = [
        ('PK1',
         'UNIQUE(numero_sala)',
         "El numero de sala no se puede repetir"),
    ]
