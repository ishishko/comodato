from odoo import api, fields, models

class ProductProduct(models.Model):
    _inherit='product.product'
    

    description_comodato = fields.Char( string='Descripcion comodato:' , related="product_tmpl_id.description_comodato" )