# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Cliente_Descuento(models.Model):

    _name = 'modulo_cine.cliente_descuento'

    numero_butaca = fields.Many2one('modulo_cine.cliente', 'numero_butaca')
    nombre = fields.Many2one('modulo_cine.cliente', 'nombre')
    numero_sala = fields.Many2one('modulo_cine.cliente', 'numero_sala')
    fecha = fields.Many2one('modulo_cine.cliente', 'fecha')
    tipo = fields.Many2one('modulo_cine.descuento', 'tipo')

    _sql_constraints = [
        ('PK6',
         'UNIQUE(numero_butaca, nombre, numero_sala, fecha)',
         "El descuento por cliente es unico"),
    ]
