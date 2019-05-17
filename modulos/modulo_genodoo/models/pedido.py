# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Pedido(models.Model):

    _name = 'genodoo.pedido'

    name = fields.Char(
        string='Nombre',
        required=True,
    )
    correo = fields.Char(
        string='Correo',
        required=True,
    )
    telefono = fields.Integer(
        string='Teléfono',
    )
    modulo = fields.Selection(
        string='Módulo deseado',
        selection=[("tienda", "Tienda"), ("resta", "Restaurante"), ("hotel", "Hotel"), ("cine", "Cine"), ("persona", "Personalizado")]
    )
    tarifa = fields.Selection(
        string='Tarifa',
        selection=[("base", "Basico"), ("avan", "Avanzado"), ("expe", "Experto")]
    )
    info_extra = fields.Char(
        string='Información adicional',
    )

