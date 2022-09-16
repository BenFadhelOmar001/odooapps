from odoo import models, fields, api


class mardi(models.Model):
     _name = 'mardii'
     _description = 'mardi description'

     name = fields.Char(string="name")
     A8_  = fields.One2many('cellul', 'sall_id_m1', string="8:00 --> 9:30", limit=1)
     A9_1 = fields.One2many('cellul', 'sall_id_m1', string="9:35 --> 11:05", limit=1)
     A10_1 = fields.One2many('cellul', 'sall_id_m1', string="11:10 --> 12:40", limit=1)
     A11_1 = fields.One2many('cellul', 'sall_id_m1', string="13:10 --> 14:40", limit=1)
     A12_1 = fields.One2many('cellul', 'sall_id_m1', string="14:45 --> 16:20", limit=1)
     A13_1 = fields.One2many('cellul', 'sall_id_m1', string="16:25 --> 17:55", limit=1)
     sal_id = fields.Many2one('emplois', string="Sall")