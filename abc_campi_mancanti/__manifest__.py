# -*- coding: utf-8 -*-
{
    'name': "ABC - abc_campi_mancanti",

    'summary': """
        Modulo che aggiunge i campi X e Y""",

    'description': """
        Modulo che aggiunge i campi X e Y
    """,

    'author': "A.B.C. srl",
    'website': "https://www.abcstrategie.it/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    "installable": True,
}
