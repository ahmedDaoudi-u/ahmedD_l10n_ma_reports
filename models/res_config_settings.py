from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    CNSS_max = fields.Float(string="Plafond Prestations Sociales",
                            config_parameter="teos_l10n_ma_reports.cnss_max")

    pour_cnss = fields.Float(string="CNSS Employe",
                             config_parameter="teos_l10n_ma_reports.cnss")

    pour_amo = fields.Float(string="AMO Employe",
                            config_parameter="teos_l10n_ma_reports.amo")
