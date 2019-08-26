from odoo import models,fields,api
from datetime import datetime
from datetime import date, timedelta

class PartnerOverdue(models.Model):
   # _name = 'res.partner'
    _inherit = 'res.partner'

    over_due_compute = fields.Float("Overdue Days",compute="cal_field",store=True)



    def cal_field(self):
        for record in self:
            account = self.env["account.move.line"].search([('partner_id.name','=',record.name)])
            lis=[]
            pro=[]
            for s in account:
                if s.full_reconcile_id:
                    pro.append(s.date_maturity)
                else:
                    val = date.today().strftime('%Y-%m-%d')
                    sal = datetime.strptime(val, '%Y-%m-%d')

                    value = s.date_maturity.strftime('%Y-%m-%d')
                    sal1 = datetime.strptime(value, '%Y-%m-%d')

                    final = sal - sal1
                    lis.append(final.days)

            lis.sort(key=int)
            if len(lis) != 0:
                a = lis[-1]
                record.overdue = a
                record.update({'overdue': a})



