from odoo import api, fields, models

class SaleOrder (models.Model):
    _inherit='sale.order'
    
    patient_id = fields.Many2one('res.partner', string='Paciente', default= False,
                                 domain=[('patient_check', '=', True)])
    