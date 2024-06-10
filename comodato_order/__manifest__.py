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
    "depends": [ "sale_renting" ],
    "data": [
        "views/res_config_settings_views.xml",
        "views/sale_temporal_recurrence_views.xml",
        "views/product_template_view.xml",
        "views/res_partner_patient.xml",
        "views/sale_order_view.xml",
        "views/sale_order_views.xml",
        "views/sale_comodato_menus.xml",

        # 'report/rental_order_report_templates.xml',
        # 'report/rental_report_views.xml',
        # 'report/rental_schedule_views.xml',
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
