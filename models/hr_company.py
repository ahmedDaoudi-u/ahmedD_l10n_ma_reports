from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime

class HrCompanydata(models.Model):

    _inherit = ['res.company']

    company_status = fields.Selection(
        [('Agricole', 'agricole'), ('Non-Agricole', 'non-agricole')],
        String="Secteur d'activité")


















