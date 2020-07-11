from odoo import api, exceptions, fields, models, _


class WizardSaleOrderConfirmAll(models.TransientModel):
    _name = "wizard.sale.order.confirm.all"

    @api.multi
    def action_sale_confirm_all(self):
        self.ensure_one()
        ids = self.env['sale.order'].browse(self._context.get('active_ids'))
        for line in ids:
            if line.state not in ['sale', 'done', 'cancel']:
                line.action_confirm()
