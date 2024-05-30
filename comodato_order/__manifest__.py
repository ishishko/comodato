# -*- coding: utf-8 -*-
{
    'name': "Comodato",

    'summary': "Manejo de contratos de comodato, entrega y devolucion",

    'description': """
Aplicacion para el manejo de comodato de pacientes a traves de empresas.
    """,

    'website': "https://www.odoo.com/app/rental",

    'category': 'Sales/Sales',
    'sequence': 160,
    'version': '1.0',

    'depends': ['base','sale'],

    'data': [],
    'application': True,
    # 'pre_init_hook': '_pre_init_rental',
    # 'assets': {
    #     'web.assets_backend': [
    #         'sale_renting/static/src/**/*',
    #     ],
    # },
    # 'license': 'GPL-3',
}
