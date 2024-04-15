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

    date_data = fields.Char(String="employee name")


    def compute_sheet(self):
        for rec in self:
            employee = rec.contract_id
            if employee:
                input_value = employee.date_start
                rec.date_data = input_value
        return super(HrPayslip, self).compute_sheet()








