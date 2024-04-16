from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime
from datetime import datetime
class HrPayslip(models.Model):

    _inherit = ['hr.payslip']

    type_payment = fields.Selection(
        [('Virement', 'virement'),
         ('Espèces', 'espèces'),
         ('Dépôt', 'dépôt'),
         ('Chèque', 'chèque'), ],
        String="Paiement Par")

    commentaire = fields.Char(String="comment about the employee")

    categorie = fields.Selection(
        [('Salarié', 'salarié')],
        String="Categories salarié")


    droit = fields.Char(String="employee name", readonly=True)

    reliquat = fields.Char(String="reliquat", readonly=True)
    pris = fields.Char(String="pris", readonly=True)
    solde = fields.Char(String="solde", readonly=True)



    def compute_sheet(self):
        for rec in self:
            employee = rec.contract_id
            time_off = rec.employee_id

            if employee and time_off:

                start_date = employee.date_start
                amount_time_off = time_off.allocation_count
                rec.pris = amount_time_off

                if start_date:
                    today_date = fields.Date.today()
                    start_date = fields.Date.from_string(start_date)
                    difference = today_date.year - start_date.year

                    if (difference * 12) <= 60:
                        time_off = min((difference * 12) * 1.5, 18)
                        rec.droit = time_off
                    else:
                        additional_accrual = (employee.number_of_years // 5) * 1.5 + 18
                        time_off += additional_accrual
                        rec.droit = time_off


        return super(HrPayslip, self).compute_sheet()








