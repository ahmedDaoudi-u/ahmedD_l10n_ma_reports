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
                    #print(start_date_month)

                    months = years * 12

                    if months <= 12:
                        numb_months = (today_date.year - start_date.year) * 12 + today_date.month - start_date.month
                        time_off = min(numb_months * 1.5, 18)
                        print(time_off)
                        rec.solde = time_off
                    else:
                        time_off = min((years // 5) * 1.5 + 18, 30)
                        rec.solde = time_off


            # Getting the name of the field and getting the values to show in the payslip
            rec_names = []
            rec_amounts = []

            salaire_net = rec.net_wage
            salaire_brut = rec.gross_wage

            rec_payslip = rec.line_ids.filtered(lambda line: line.appears_on_payslip)
            for names in rec_payslip:

                rec_amounts.append(names.amount)
                rec_names.append(names.name)

            #print(rec_names)
            #print(rec_amounts)


            for index, name in enumerate(rec_names):
                if name == 'Gross':
                    rec_amounts[index] = 1000


        return super(HrPayslip, self).compute_sheet()

    def _compute_hours_per_day(self):


        super(HrPayslip,self)._compute_hours_per_day()



    #Setting up the limits of the hour worked during the day
    def action_refresh_from_work_entries(self):
    

        # Setting up the maximum over-time hours per day
        current_record_id = self.id
        payslip_record = self.env['hr.payslip'].browse(current_record_id)
        worked_days_records = payslip_record.worked_days_line_ids

        for worked_days_record in worked_days_records:
            if worked_days_record.code == 'OVERTIME':
                over_time_regular_hours = min(2, worked_days_record.number_of_hours)
                worked_days_record.number_of_hours = over_time_regular_hours


        #overtime_worked_days = self.env['hr.payslip.worked_days']

        #current_record_id = self.id
        #total_overtime_hours = 0
        # Assuming self.env['hr.payslip.worked_days'] is a recordset
        #worked_days_record = self.env['hr.payslip.worked_days'].search([('payslip_id', '=', current_record_id)],
        #                                                               limit=2)
        #over_time_regular_hours = worked_days_record.filtered(lambda wd: wd.code == 'OVERTIME').number_of_hours

        #over_time_regular_hours = min(2, over_time_regular_hours)  # Cap at 2 hours
        #worked_days_record.write({'number_of_hours': over_time_regular_hours})



        #hours_per_day = self._get_worked_day_lines_hours_per_day()
        #worked_hours_month = hours_per_day*26

        #if worked_hours_month < 200:
        #    print(worked_hours_month)
        #else:
        #    pass
        #payslips = self.worked_days_line_ids.filtered(lambda line: line)
        #work_type = payslips.work_entry_type_id.name
        #hours_worked = payslips.number_of_hours
        #hours_worked = 45

        #return hours_worked

        #print(work_type)
        #print(number_of_hours)

        return super(HrPayslip,self).action_refresh_from_work_entries()








