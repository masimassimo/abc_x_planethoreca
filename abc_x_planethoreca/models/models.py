# -*- coding: utf-8 -*-

from odoo import models, fields, api

class abc_x_planethoreca(models.Model):
     _name = 'abc_x_planethoreca.abc_x_planethoreca'
     _description = 'abc_x_planethoreca.abc_x_planethoreca'

class PosConfig(models.Model):
    _name = "pos.config"
    _inherit = "pos.config"
    
    fattura_per_tutti = fields.Boolean(string="Fatturapertutti", default = False, store=True)
    #Commentino

class ResPartner(models.Model):
    _name = "res.partner"
    _inherit = 'res.partner'
    
    fax = fields.Char(string="FAX",store=True)

class ProductTemplate(models.Model):
    _name = "product.template"
    _inherit = "product.template"
    
    weight_netto = fields.Float(string="Peso Netto", default = 0.0, store=True)
    weight_netto_uom = fields.Char(string="", readonly=True, default="kg")
     
    width = fields.Float(string="Larghezza", default = 0.0, store=True)
    width_uom = fields.Char(string="", readonly=True, default="cm")
    
    height = fields.Float(string="Altezza", default = 0.0, store=True)
    height_uom = fields.Char(string="", readonly=True, default="cm")
    
    depth = fields.Float(string="Lunghezza", default = 0.0, store=True)
    depth_uom = fields.Char(string="", readonly=True, default="cm")
     
    weight = fields.Float(string="Peso Lordo", default = 0.0, store=True, readonly=False, store_true=True)
