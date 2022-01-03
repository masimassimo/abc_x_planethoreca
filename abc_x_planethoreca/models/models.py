# -*- coding: utf-8 -*-

from odoo import models, fields, api

class abc_x_planethoreca(models.Model):
     _name = 'abc_x_planethoreca.abc_x_planethoreca'
     _description = 'abc_x_planethoreca.abc_x_planethoreca'

class PosConfig(models.Model):
    _name = "pos.config"
    _inherit = "pos.config"
    
    fattura_per_tutti = fields.Boolean(string="Fatturapertutti", default = False)

class ResPartner(models.Model):
    _name = "res.partner"
    _inherit = 'res.partner'
    
    fax = fields.Char(string="FAX",store=True)

class ProductTemplate(models.Model):
    _name = "product.template"
    _inherit = "product.template"
    
    width = fields.Float(string="Width", default = 0.0)
    width_uom = fields.Char(string="", readonly=True, default="m")
    
    height = fields.Float(string="Height", default = 0.0)
    height_uom = fields.Char(string="", readonly=True, default="m")
    
    depth = fields.Float(string="Depth", default = 0.0)
    depth_uom = fields.Char(string="", readonly=True, default="m")
