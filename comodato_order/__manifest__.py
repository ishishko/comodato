# -*- coding: utf-8 -*-
{
    "name": "Comodato",
    "summary": "Manejo de contratos de comodato, entrega y devolucion",
    "description": """
Aplicacion para el manejo de comodato de pacientes a traves de empresas.
Se agrega el campo patient_check a la vista de res.partner.
    """,
    "autor": "Ignacio Shishko",
    "website": "https://www.hitofusion.com/",
    "category": "Sales/Sales",
    "sequence": 160,
    "version": "17.0.0.0.0",
    "depends": ["base", "sale"],
    "data": [
        "views/res_partner_patient.xml",
        "views/sale_order_view.xml",
        "views/sale_comodato_menus.xml",
        "views/sale_order_views.xml",
    ],
    "installable": True,
    "application": True,
    # 'pre_init_hook': '_pre_init_rental',
    # 'assets': {
    #     'web.assets_backend': [
    #         'sale_renting/static/src/**/*',
    #     ],
    # },
    "license": "GPL-3",
}
