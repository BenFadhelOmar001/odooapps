from odoo import models, fields, api


class matieres(models.Model):
     _name = 'matiere'
     _description = 'matieres description'

     matière = fields.Char(string="matière")
     type_matiere = fields.Selection([('cours','Cours'),('td','TD'),('tp','TP')], string="type_matiere")
     groupe_etudiants = fields.Many2one('groupe', string="groupe_etudiants", required='true')
     name = fields.Char(compute="_onchange_proc", string="name")

     @api.depends('matière', 'type_matiere')
     def _onchange_proc(self):
          for record in self:
               record.name = record.type_matiere + " "+record.matière