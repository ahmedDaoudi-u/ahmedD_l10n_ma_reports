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



