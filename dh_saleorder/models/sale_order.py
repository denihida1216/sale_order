from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.onchange('user_id')
    @api.depends('user_id')
    def _sales_person(self):
        res = {}
        check = self.env['res.users'].has_group('dh_saleorder.group_sale_order_salesperson_only')
        if check:
            res['domain'] = {'partner_id': [('user_id', '=', self.user_id.id)]}
        return res

    @api.multi
    def action_confirm(self):
        imediate_obj = self.env['stock.immediate.transfer']
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            warehouse = order.warehouse_id
            if warehouse.is_delivery_set_to_done and order.picking_ids:
                for picking in self.picking_ids:
                    picking.action_confirm()
                    picking.action_assign()
                    imediate_rec = imediate_obj.create({'pick_ids': [(4, order.picking_ids.id)]})
                    imediate_rec.process()

            self._cr.commit()

            if warehouse.create_invoice and not order.invoice_ids:
                order.action_invoice_create()

            if warehouse.validate_invoice and order.invoice_ids:
                for invoice in order.invoice_ids:
                    invoice.action_invoice_open()

        return res