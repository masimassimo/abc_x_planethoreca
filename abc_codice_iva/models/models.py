# -*- coding: utf-8 -*-
from odoo import models, fields, api


class abc_codice_iva(models.Model):
    _name = 'abc_codice_iva.abc_codice_iva'
    _description = 'abc_codice_iva.abc_codice_iva'
    
#Eredito il modulo account.tax per accedervi e creare il nuovo campo codice_iva.
class accountTax(models.Model):
    _name = "account.tax"
    _inherit = "account.tax"
    
    codice_iva = fields.Char(string = "Codice Iva", store = True)
