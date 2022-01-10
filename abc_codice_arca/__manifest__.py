# -*- coding: utf-8 -*-
{
    'name': "ABC - abc_codiceArca",

    'summary': """
        Modulo che permette crea il campo Codice Arca nell'anagrafica Contatto.""",

    'description': """
        Modulo che permette crea il campo Codice Arca nell'anagrafica Contatto.
    """,

    'author': "A.B.C srl",
    'website': "https://www.abcstrategie.it/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Partners',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    "installable": True,
}
