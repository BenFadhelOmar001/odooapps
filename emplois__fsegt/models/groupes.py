from odoo import models, fields, api


class groupes(models.Model):
     _name = 'groupe'
     _description = 'groupes description'

     psudo = fields.Char(string="Psudo_name", required='true')
     annee = fields.Selection([('1er','1er'),('2éme','2éme'),('3éme','3éme')], string="Année", required='true')
     groupe = fields.Selection([('A','A'),('B','B'),('C','C')], string="groupe", required='true')
     name = fields.Char(compute="_onchange_proc", string="name", required='true')

     @api.depends('annee', 'psudo', 'groupe')
     def _onchange_proc(self):
          for record in self:
               record.name = record.annee + " année "+record.psudo+" groupe " + record.groupe