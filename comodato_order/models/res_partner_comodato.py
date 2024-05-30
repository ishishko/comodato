from odoo import api, fields, models

class ResPartner_old_id (models.Model):
    _inherit='res.partner'
    
    patient = fields.Boolean(string='Paciente', default= False )