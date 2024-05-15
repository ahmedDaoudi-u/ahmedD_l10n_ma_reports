from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime

class HrConge(models.Model):

    _inherit = ['hr.employee']


    cnss_max_pres = fields.Char(string='Max Prestation sociale(DH)', compute='_compute_your_field_max_cnss')
    pour_cnss = fields.Char(string='Taux Cotisation CNSS(%)', compute='_compute_your_field_cnss')
    pour_amo = fields.Char(string='Taux Cotisation AMO(%)', compute='_compute_your_field_amo')
    max_frais_pro_mensuel = fields.Char(string='Max Frais Pro Mensuel(DH)', compute='_compute_your_frais_pro_mensu')

    @api.onchange('company_id.company_status')
    def onchange_company_status(self):
        employees = self.env['hr.employee'].search([])
        hours = employees.mapped('resource_calendar_id')
        status = self.company_status

        if status == "Agricole":
            hours.name = "Heures de travail par défaut à 44 heures par semaine"
        else:
            hours.name = "Heures de travail par défaut à 48 heures par semaine"





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


    def _compute_your_frais_pro_mensu(self):
        config_parameter_amo = self.env['ir.config_parameter'].sudo().get_param('teos_l10n_ma_reports.frais_pro')
        for record in self:
            record.max_frais_pro_mensuel = config_parameter_amo
















