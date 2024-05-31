from odoo import api, fields, models

class ProductTemplate (models.Model):
    _inherit='product.template'
    

    description_comodato = fields.Char( string='Descripcion comodato:', size=255, default= False )