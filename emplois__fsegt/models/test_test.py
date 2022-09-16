from odoo import models, fields, api
import re
from odoo.exceptions import ValidationError


class test_test(models.Model):
    _inherit = 'hr.employee'
    champ_1 = fields.Char(string="champ_1")
    champ_2 = fields.Char(string="champ_2")
    champ_3 = fields.One2many('test.test.2', 'Colléges', string="Colléges")


    @api.constrains('work_email')
    def validate_mail(self):
        if self.work_email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.work_email)
            if match == None:
                raise ValidationError('Not a valid E-mail')



