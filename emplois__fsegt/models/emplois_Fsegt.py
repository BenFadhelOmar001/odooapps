from odoo import models, fields, api


class emplois__fsegt(models.Model):
     _name = 'emplois'
     _description = 'emplois__fsegt description'
     select_groupe = fields.Many2one('groupe', string="groupe", required='true')
     Lundi = fields.One2many('lundii', 'sall_id', string="Lundi")
     Mardi = fields.One2many('mardii', 'sal_id', string="Mardi")
     Merecredi = fields.One2many('merecredii', 'salleid', string="Merecredi")
     Jeudi = fields.One2many('jeudii', 'sald', string="Jeudi")
     Vendredi = fields.One2many('vendredii', 'se_id', string="Vendredi")
     Samedi = fields.One2many('samedii', 'leid', string="Samedi")

