# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'


    is_comodato = fields.Boolean(string="Documento Predefinido", default=False)
    # comodato_document = 

    @api.onchange('extra_hour')
    def _onchange_extra_hour(self):
        self.env['ir.property']._set_default("extra_hourly", "product.template", self.extra_hour)

    @api.onchange('extra_day')
    def _onchange_extra_day(self):
        self.env['ir.property']._set_default("extra_daily", "product.template", self.extra_day)
