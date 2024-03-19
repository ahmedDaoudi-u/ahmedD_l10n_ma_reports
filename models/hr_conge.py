from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime

class HrConge(models.Model):

    _inherit = ['hr.leave.accrual.plan']

    reliquat = fields.Float(String="get the time off the last period")

    droit = fields.Float(String="number of days that teh employee can have")


