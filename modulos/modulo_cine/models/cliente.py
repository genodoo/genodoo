# -*- coding: utf-8 -*-

from odoo import models, fields, api

class (models.Model):

    _name = 'modulo_cine.cliente'

    numero_butaca = fields.Char(string='Numero de Butaca')
    nombre = fields.Many2one('modulo_cine.reproduccion', 'nombre')
    numero_sala = fields.Many2one('modulo_cine.reproduccion', 'numero_sala')
    fecha = fields.Many2one('modulo_cine.reproduccion', 'fecha')
    edad = fields.Integer(string = 'Edad')

    _sql_constraints = [
        ('PK5',
         'UNIQUE(numero_butaca, nombre, numero_sala)',
         "No puede existir el mismo cliente"),
    ]
