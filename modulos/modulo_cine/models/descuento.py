# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Descuento(models.Model):

    _name = 'modulo_cine.descuento'

    tipo = fields.Char(string='Tipo de Descuento', required=True)
    valor = fields.Float(string='% Descuento', required=True)
    edad_aplicable = fields.Integer(string='Edad Aplicable')

    _sql_constraints = [
        ('PK3',
         'UNIQUE(tipo)',
         "El tipo de descuento no se puede repetir"),
    ]
