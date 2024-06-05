from odoo import api, fields, models

class SaleOrderLine (models.Model):
    _inherit='sale.order.line'
    

    comodato_check = fields.Boolean(string='Comodato', related='order_id.comodato_check')

    @api.depends('product_id')
    def _compute_name(self):
        super()._compute_name()

        for line in self:
            if line.comodato_check:
                line.name = line.product_id.comodato_description
                continue