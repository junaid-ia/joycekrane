from odoo import models,fields,api
from datetime import datetime
from datetime import date, timedelta

class PartnerOverdue(models.Model):
   # _name = 'res.partner'
    _inherit = 'res.partner'

    over_due_compute = fields.Float("Overdue Days",compute="cal_field",store=True)
    over_due_compute1 = fields.Float("Overdue Days", related="over_due_compute",store=True)


    @api.depends('over_due_compute')
    def _compute_fieldvalue(self):
        for each in self:
            each.over_due_compute1 = each.over_due_compute



    def cal_field(self):
        for record in self:
            account = self.env["account.invoice"].search([('partner_id.name','=',record.name),('date_due','<',date.today())])

            lis=[]
            pro=[]
            for s in account:
                val = date.today().strftime('%Y-%m-%d')
                sal = datetime.strptime(val, '%Y-%m-%d')

                value = s.date_due.strftime('%Y-%m-%d')
                sal1 = datetime.strptime(value, '%Y-%m-%d')

                final = sal - sal1
                lis.append(final.days)

            lis.sort(key=int)
            if len(lis) != 0:
                a = lis[-1]
                record.over_due_compute1 = a
                record.over_due_compute = a
                record.update({'over_due_compute': a})
                record.update({'over_due_compute1': a})




