from odoo import models,fields,api
from datetime import datetime
from datetime import date, timedelta

class PartnerOverdue(models.Model):
    _inherit = "res.partner"

    overdue = fields.Char('Overdue Days',compute='cal_field')



    def cal_field(self):
        account = self.env["account.move.line"].search([('partner_id.name','=',self.name)])
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
        a = lis[-1]
        self.overdue = a
        self.update({'overdue': a})



