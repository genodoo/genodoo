# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HotelRoom(models.Model):

    _name = "hotel.room"

    name = fields.Char(
        string="Reference", 
        readonly=True,
    )
    room_number = fields.Char(
        string="Room Number", 
        required=True,
        default="0"
    )
    room_floor = fields.Char(
        string="Room Floor",
        required=True,
        default="0"
    )
    room_size = fields.Integer(
        string="Size",
        required=True,  
    )

    @api.model
    def create(self, vals):
        vals["name"] = vals["room_number"] + "-" + vals["room_floor"]
        return super(HotelRoom, self).create(vals)


class HotelBook(models.Model):
    _name = "hotel.book"

    name = fields.Char(string="Reference")
    room_id = fields.Many2one(
         string='Room',
         comodel_name='hotel.room',
    )
    customer_id = fields.Many2one(
        string='Customer',
        comodel_name='res.partner',
    )
    date_in = fields.Datetime(
        string='Date IN',
    )
    date_out = fields.Datetime(
        string='Date OUT',
    )
    
     