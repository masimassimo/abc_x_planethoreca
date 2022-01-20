# -*- coding: utf-8 -*-
from odoo import models, fields, api


class abc_codice_arca(models.Model):
    _name = 'abc_codice_arca.abc_codice_arca'
    _description = 'abc_codice_arca.abc_codice_arca'

#Accedo al modulo res.partner per creare il campo codice_arca.
class ResPartner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"
    
    codice_arca = fields.Char(string="Codice Arca", store=True)

class ProductTemplate(models.Model):
    _name = "product.template"
    _inherit = "product.template"
    
    codice_arca = fields.Char(string="Codice Arca", store=True)

class ProductProduct(models.Model):
    _name = "product.product"
    _inherit = "product.product"
    
    codice_arca = fields.Char(string="Codice Arca", store=True)
