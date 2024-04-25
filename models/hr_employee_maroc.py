from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime

class HrConge(models.Model):

    _inherit = ['hr.employee']


    cnss_max_pres = fields.Char(string='Max Prestation sociale', compute='_compute_your_field_max_cnss')
    pour_cnss = fields.Char(string='Taux Cotisation CNSS', compute='_compute_your_field_cnss')
    pour_amo = fields.Char(string='Taux Cotisation AMO', compute='_compute_your_field_amo')

    # defining the function that would that the value of the settings and get it to the users
    def _compute_your_field_max_cnss(self):
        config_parameter_max_cnss = self.env['ir.config_parameter'].sudo().get_param('teos_l10n_ma_reports.cnss_max')
        for record in self:
            record.cnss_max_pres = config_parameter_max_cnss


    def _compute_your_field_cnss(self):
        config_parameter_cnss = self.env['ir.config_parameter'].sudo().get_param('teos_l10n_ma_reports.cnss')
        for record in self:
            record.pour_cnss = config_parameter_cnss



    def _compute_your_field_amo(self):
        config_parameter_amo = self.env['ir.config_parameter'].sudo().get_param('teos_l10n_ma_reports.amo')
        for record in self:
            record.pour_amo = config_parameter_amo
















