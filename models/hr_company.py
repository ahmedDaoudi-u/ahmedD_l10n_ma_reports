from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime

class HrCompanydata(models.Model):

    _inherit = ['res.company']

    company_status = fields.Selection(
        [('Agricole', 'agricole'), ('Non-Agricole', 'non-agricole')],
        String="Secteur d'activité")


    @api.onchange('company_status')
    def update_working_hours(self):
            employees = self.env['hr.employee'].search([])
            hours = employees.mapped('resource_calendar_id')
            status = self.company_status
            if status == "agricole":
                hours.name = "Standard 40 hours/week"
            else:
                hours.name = "testing"











