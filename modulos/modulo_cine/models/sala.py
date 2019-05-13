# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Sala(models.Model):

    _name = 'cine.sala'

    room_number = fields.Integer(string='Sala Número', required=True)
    capacity = fields.Integer(string='Capacidad', required=True)

    _sql_constraints = [
        ('PK1',
         'UNIQUE(room_number)',
         "El numero de sala no se puede repetir"),
    ]
