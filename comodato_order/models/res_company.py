# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    is_comodato_sign = fields.Boolean(string="Documento Predeterminado")
    
    comodato_sign_tmpl_id = fields.Many2one(
        "sign.template",
        string="Default Document Template for Rentals",
        help="This document template will be selected by default when signing "
        "documents from a rental order. You should select a template accessible "
        "to all Sign users.",
    )
