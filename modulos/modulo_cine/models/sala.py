# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Sala(models.Model):

    _name = 'cine.sala'

    name = fields.Char(string='Referencia', readonly=True)
    room_number = fields.Integer(string='Sala Número', required=True)
    capacity = fields.Integer(string='Capacidad', required=True)

    _sql_constraints = [
        ('PK1',
         'UNIQUE(room_number)',
         "El numero de sala no se puede repetir"),
    ]

    @api.onchange('room_number')
    @api.depends('room_number')
    def generate_name(self):
        self.write({"name": 'Sala Nº' + str(self.room_number)}) 
    