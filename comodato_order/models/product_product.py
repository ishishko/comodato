from odoo import api, fields, models

class ProductTemplate (models.Model):
    _inherit='product.product'
    

    description_comodato = fields.Char( string='Descripcion comodato:' )