from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime

class HrConge(models.Model):

    _inherit = ['hr.leave.accrual.plan']

    reliquat = fields.Float(String="prendre congé des dernières période",default="0", readonly=True)

    droit = fields.Float(String="nombre de congés que l'employé a droit",default="18", readonly=True)









