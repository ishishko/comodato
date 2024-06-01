from odoo import api, fields, models

class ResPartnerPatient (models.Model):
    _inherit='res.partner'
    
    patient_check = fields.Boolean(string='Paciente', default= False )