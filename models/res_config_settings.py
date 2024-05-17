from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    cnss_max = fields.Float(string="Plafond Prestations Sociales",
                            config_parameter="teos_l10n_ma_reports.cnss_max")

    pour_cnss = fields.Float(string="CNSS Employés",
                             config_parameter="teos_l10n_ma_reports.cnss")

    pour_amo = fields.Float(string="AMO Employés",
                            config_parameter="teos_l10n_ma_reports.amo")

    max_frais_pro_mensuel = fields.Float(string="Max Frais Professionel Mensuel",
                            config_parameter="teos_l10n_ma_reports.frais_pro")

    max_frais_pro_annuel = fields.Float(string="Max Frais Professionel Annuel",
                            config_parameter="teos_l10n_ma_reports.frais_pro_ans")

    payslip_table_bg_color = fields.Char("Couleur du fond de la table", default="#D7E4C0")
    show_company_address = fields.Boolean("Afficher l’adresse de l’entreprise", default=True)
    show_company_website = fields.Boolean("Afficher le site Web de l’entreprise", default=True)

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('payslip_table_bg_color', self.payslip_table_bg_color)
        self.env['ir.config_parameter'].set_param('show_company_address', self.show_company_address)
        self.env['ir.config_parameter'].set_param('show_company_website', self.show_company_website)


    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(
            payslip_table_bg_color=self.env['ir.config_parameter'].sudo().get_param('payslip_table_bg_color', default="#D7E4C0"),
            show_company_address=self.env['ir.config_parameter'].get_param('show_company_address',
                                                                           default=True) == 'True',
            show_company_website=self.env['ir.config_parameter'].get_param('show_company_website',
                                                                           default=True) == 'True',
        )
        return res