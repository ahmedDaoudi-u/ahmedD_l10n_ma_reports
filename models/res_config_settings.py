from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    CNSS_max = fields.Float(string="Plafond Prestations Sociales",
                            config_parameter="teos_l10n_ma_reports.cnss_max")

    pour_cnss = fields.Float(string="CNSS Employés",
                             config_parameter="teos_l10n_ma_reports.cnss")

    pour_amo = fields.Float(string="AMO Employés",
                            config_parameter="teos_l10n_ma_reports.amo")

    max_frais_pro_mensuel = fields.Float(string="Max Frais Professionel Mensuel",
                            config_parameter="teos_l10n_ma_reports.frais_pro")

    max_frais_pro_annuel = fields.Float(string="Max Frais Professionel Annuel",
                            config_parameter="teos_l10n_ma_reports.frais_pro_ans")
