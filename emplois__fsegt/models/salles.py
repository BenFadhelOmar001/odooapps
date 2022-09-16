
from odoo import models, fields, api


class salles(models.Model):
    _name = 'salle'
    _description = 'salles description'


    type_salle = fields.Selection([('amphi', 'Amphi'), ('mini_amphi', 'mini_Amphi'), ('td', 'TD'), ('tp', 'TP')], string="type_salle")
    num_salle = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '12'), ('13', '13')], string="num_salle")
    name = fields.Char(compute="_onchange_proc", string="name")


    @api.depends('num_salle','type_salle')
    def _onchange_proc(self):
        for record in self:
            record.name = record.type_salle + " " + record.num_salle
