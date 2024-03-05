from odoo import models, fields ,api

class HrPayslip(models.Model):

    _inherit = ['hr.contract']

    type_payment = fields.Selection(
        [('Virement', 'virement'),
         ('Espèces', 'espèces'),
         ('Dépôt', 'dépôt'),
         ('Chèque', 'chèque'),],
        String="Par")



