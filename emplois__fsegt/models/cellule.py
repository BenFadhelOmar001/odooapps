from odoo import models, fields, api


class cellule(models.Model):
     _name = 'cellul'
     _description = 'cellule description'

     select_salle = fields.Many2one('salle', string=" salle", limit=1)
     select_matière = fields.Many2one('matiere', string=" matiere", limit=1)
     salle_id_l1 = fields.Many2one('lundii', string="Sall", limit=1)

     sall_id_m1 = fields.Many2one('mardii', string="Sal", limit=1)

     sal_id_r1 = fields.Many2one('merecredii', string="Sl", limit=1)

     sa_id_j1 = fields.Many2one('jeudii', string="S", limit=1)

     s_id_v1 = fields.Many2one('vendredii', string="Salld", limit=1)

     salle_i_s1 = fields.Many2one('samedii', string="Salls", limit=1)


