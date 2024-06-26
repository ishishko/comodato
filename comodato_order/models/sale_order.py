from odoo import api, fields, models

class SaleOrder (models.Model):
    _inherit='sale.order'
    
    patient_id = fields.Many2one('res.partner', string='Paciente', domain=[('patient_check', '=', True)], required=True)

    comodato_check = fields.Boolean(string='Comodato', default= False )

