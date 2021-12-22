# -*- coding: utf-8 -*-
{
    'name': "abc_x_planethoreca",

    'summary': """Modulo che contiene le modifiche apportate su Planet Horeca, relativo a Fatturapertutti, template DDT, 
    Preventivo/Ordine di vendita, Fattura, Point of Sale""",

    'description': """
        Modulo che contiene le modifiche apportate su Planet Horeca, relativo a Fatturapertutti, template DDT, 
    Preventivo/Ordine di vendita, Fattura, Point of Sale
    """,

    'author': "A.B.C. srl",
    'website': "https://www.abcstrategie.it/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale', 'sale_management', 'pos_sale', 'sale_enterprise', 'sale_margin', 'sale_stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/preventivo_ordineVendita.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
