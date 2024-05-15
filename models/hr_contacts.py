from odoo import models, fields, api


class HrContacts(models.Model):

    _inherit = ['hr.contract']

    hourly_wage_employee = fields.Float(String="Taux Horraire",compute="_compute_hourly_wage")


    def _compute_hourly_wage(self):
        for rec in self:
            employees = self.env['hr.contract'].search([])

            hourly_wage = employees.hourly_wage
            wage_type = employees.wage_type
            wage = employees.wage

            if wage_type =='hourly wage':
                rec.hourly_wage_employee = hourly_wage

            else:
                hour_cost = round(wage / 191, 2)
                rec.hourly_wage_employee = hour_cost









