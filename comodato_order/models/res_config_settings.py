# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    is_comodato_sign = fields.Boolean(related="company_id.is_comodato_sign", 
                                      string="Documento Predeterminado",
                                     readonly=False)

    comodato_sign_tmpl_id = fields.Many2one(
        "sign.template",
        related="company_id.comodato_sign_tmpl_id",
        string="Seleccione documento",
        help="Set a default document template for all rentals in the current company",
        readonly=False,
    )