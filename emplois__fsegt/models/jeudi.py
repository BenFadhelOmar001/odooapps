from odoo import models, fields, api


class jeudi(models.Model):
     _name = 'jeudii'
     _description = 'jeudi description'

     name = fields.Char(string="name")
     A89  = fields.One2many('cellul', 'sa_id_j1', string="8:00 --> 9:30", limit=1)
     A910 = fields.One2many('cellul', 'sa_id_j1', string="9:35 --> 11:05", limit=1)
     A1011 = fields.One2many('cellul', 'sa_id_j1', string="11:10 --> 12:40", limit=1)
     A1112 = fields.One2many('cellul', 'sa_id_j1', string="13:10 --> 14:40", limit=1)
     A1213 = fields.One2many('cellul', 'sa_id_j1', string="14:45 --> 16:20", limit=1)
     A1314 = fields.One2many('cellul', 'sa_id_j1', string="16:25 --> 17:55", limit=1)
     sald = fields.Many2one('emplois', string="Sall")