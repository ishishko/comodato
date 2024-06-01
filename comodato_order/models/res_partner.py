from odoo import api, fields, models

class ResPartnerPatient (models.Model):
    _inherit='res.partner'
    
    patient = fields.Boolean(string='Paciente', default= False )