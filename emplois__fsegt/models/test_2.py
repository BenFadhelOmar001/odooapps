from odoo import models, fields, api


class test(models.Model):
    _name = 'test.test.2'
    _description = 'test 2'

    Colléges = fields.Many2one('hr.employee', string="name")
    #Collége = fields.Many2many('hr.employee', 'test_employee_rel', 'test_id', 'employee_id', string="name")
    phone = fields.Char(related="Colléges.work_phone", string="Téléphone")
    #phone = fields.Many2one('hr.employee', string="Téléphone")

    #@api.depends('Colléges')
    #def _onchange_proc(self):
        #for record in self:
            #record.phone = record.Colléges.work_phone

    #@api.onchange(phone)
    #def _onchange_proc(self):

        #if self.Colléges:
            #idd = self.Colléges.work_phone
            #return {"domain": {'work_phone':[('work_phone', '=', idd)]}}

