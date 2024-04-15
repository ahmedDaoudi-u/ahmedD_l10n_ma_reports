from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
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

    employee_name = fields.Char(String="employee name")


    def compute_sheet(self):
        for rec in self:
            employee = rec.employee_id
            if employee:
                input_value = employee.name
                rec.employee_name = input_value
        # Call the original method if needed
        return super(HrPayslip, self).compute_sheet()








