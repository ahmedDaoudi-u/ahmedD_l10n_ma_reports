from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    CNSS_max = fields.Float(string="Plafond Prestations Sociales")
    pour_cnss = fields.Float(string="CNSS Employe")
    pour_amo = fields.Float(string="AMO Employe")