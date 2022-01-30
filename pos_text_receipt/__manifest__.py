# -*- coding: utf-8 -*-
{
    'name': "ABC - abc_pos_text",

    'summary': """
        Modulo che permette di stampare lo scontrino in TXT dopo averlo validato alla cassa.""",

    'description': """
        Modulo che permette di stampare lo scontrino in TXT dopo averlo validato alla cassa.
    """,

    'author': "A.B.C Srl",
    'website': "https://www.abcstrategie.it/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Point of Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/templates.xml'
    ],
    'qweb': [
        'static/src/xml/pos.xml',
    ],
    'images': [
        'static/description/download.jpg',
    ],
    'installable': True,
    'auto_install': False,
}
