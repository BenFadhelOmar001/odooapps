from odoo import models, fields, api


class lundi(models.Model):
     _name = 'lundii'
     _description = 'lundi description'

     name = fields.Char(string="name")
     A8_9  = fields.One2many('cellul', 'salle_id_l1', string="8:00 --> 9:30", limit=1)
     A9_10 = fields.One2many('cellul', 'salle_id_l1', string="9:35 --> 11:05", limit=1)
     A10_11 = fields.One2many('cellul', 'salle_id_l1', string="11:10 --> 12:40", limit=1)
     A11_12 = fields.One2many('cellul', 'salle_id_l1', string="13:10 --> 14:40", limit=1)
     A12_13 = fields.One2many('cellul', 'salle_id_l1', string="14:45 --> 16:20", limit=1)
     A13_14 = fields.One2many('cellul', 'salle_id_l1', string="16:25 --> 17:55", limit=1)
     sall_id = fields.Many2one('emplois', string="Sall")
     #salle_id = fields.Many2one('salle', string="Sall")
     #select_salle = fields.One2many('salle', string="Salle")