# -*- coding: utf-8 -*-

from odoo import models, fields, api


class abc_campi_mancanti(models.Model):
    _name = 'abc_campi_mancanti.abc_campi_mancanti'
    _description = 'abc_campi_mancanti.abc_campi_mancanti'

class PosOrder(models.Model):
    _name = "pos.order"
    _inherit = "pos.order"
    
    data_fattura_per_tutti = fields.Char(string="Data Fatturapertutti", store=True)
    progressivo_fattura_per_tutti = fields.Char(string = "Progressivo Fatturapertutti", store=True)