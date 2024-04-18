from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime

class HrConge(models.Model):

    _inherit = ['hr.employee']

    droit = fields.Char(String="employee name", readonly=True)

    reliquat = fields.Char(String="reliquat", readonly=True)
    pris = fields.Char(String="pris", readonly=True)
    solde = fields.Char(String="solde", readonly=True)









