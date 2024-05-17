from odoo import models, fields, api

class BasePayslipLayout(models.TransientModel):
    _inherit = 'base.document.layout'

    '''#preview = fields.Html(compute="_compute_preview", sanitize=False)

    # def _compute_preview(self):
    #     styles = self._get_asset_style()
    #     return styles
    #
    #     super(Documentpayslip, self)._compute_preview()'''

    def _get_asset_style(self):
        payslip_style = self.env['ir.qweb']._render('payslip_template_inherited', {
            'company_ids': self,
        }, raise_if_not_found=False)

        return payslip_style

        super(Documentpayslip, self)._get_asset_style()