# -*- coding: utf-8 -*-

from odoo import models, fields, api

class abc_x_planethoreca(models.Model):
     _name = 'abc_x_planethoreca.abc_x_planethoreca'
     _description = 'abc_x_planethoreca.abc_x_planethoreca'

class PosConfig(models.Model):
    _name = "pos.config"
    _inherit = "pos.config"
    
    fattura_per_tutti = fields.Boolean(string="Fatturapertutti", default = False)
    
#Eredito il modulo "SaleOrder" per accedere alla vista.
class SaleOrder(models.Model):
    _inherit = 'sale.order'

    nominativo_di_riferimento = fields.Many2one(
        'res.partner', string='Nominativo di riferimento', readonly=True,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        required=False, change_default=True, index=True, tracking=1,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id), ('parent_id', '=', partner_id)]",)

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
