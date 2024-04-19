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

    #Defining the cron function for Droit Calculation
    def calcule_droit(self):
        employees = self.env['hr.payslip'].search([])
        current_day = employees.mapped('date_to')
        for dates in current_day:
            months = fields.Date.from_string(dates).month
            time_off = months * 1.5
            employees.droit = time_off


        """for employee in employees:
            get_dat_emp = employee.employee_id
            current_date = get_dat_emp.date_from
            date = fields.Date.from_string(current_date)
            months = date.month

            employees.droit = months"""

    # Defining the function for Solde calculation
    def compute_sheet(self):
        for rec in self:
            #Getting the modules we need
            employee = rec.contract_id
            time_off = rec.employee_id

            if employee and time_off:
                # Getting the fields necessary (typical the 4 fields)
                start_date = employee.date_start
                # This for  the pris but we need to add the exact field(checking...)
                # amount_time_off = time_off.allocation_count
                # rec.pris = amount_time_off

                # This block of code is for the field PRIS(checked)
                if start_date:
                    # getting the todays date
                    today_date = fields.Date.today()
                    # getting the starting date of work from the employee contract
                    start_date = fields.Date.from_string(start_date)
                    # calculate the number of years & months
                    years = today_date.year - start_date.year
                    start_date_month = start_date.month
                    print(start_date_month)

                    months = years * 12

                    if months <= 12:
                        numb_months = (today_date.year - start_date.year) * 12 + today_date.month - start_date.month
                        time_off = min(numb_months * 1.5, 18)
                        print(time_off)
                        rec.solde = time_off
                    else:
                        time_off = min((years // 5) * 1.5 + 18, 30)
                        rec.solde = time_off

        return super(HrPayslip, self).compute_sheet()








