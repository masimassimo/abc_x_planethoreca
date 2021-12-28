# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests
from prestashop_api import PrestashopApi
from collections import OrderedDict
import xmlrpc.client
import json
import logging
import re as reg

_logger = logging.getLogger(__name__)


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
    
    import re as reg
    
    def invioDatiPS(self, idOdoo, firstname, lastname, email,state_id):
        
        apiPS = PrestashopApi('https://stage.planethoreca.it:443/api', 'A5WBAUB6TF2CRGCTR29HGAXMKQ19I4D4')
        res=apiPS.get('customers?filter[id_odoo]=['+str(idOdoo)+']')
        print(dict(res)['customers'])

        if(dict(res)['customers'] is None): #Se è un nuovo contatto
            idPresta=0

        else:
            id_confronto=dict(res)['customers']['customer']
            idPresta=dict(id_confronto)['@id']

        if(idPresta!=0):

            data = {'customer': {'id':int(idPresta), 'active': 1, 'firstname': firstname, 'lastname':lastname,'email':email,'passwd':"", 'id_odoo': idOdoo,'id_shop':1, 'id_shop_group':1}}
            res = apiPS.edit('customers/'+str(idPresta), data)['customer']
            print(res['id'])

        else:
            
            
            if(state_id!=-1 and (state_id==404 or state_id==373 or state_id==306)): #TRAPANI PALERMO AGRIGENTO
                group=5
            else:
                group=4
           
            data = {'customer': {'active': 1, 'firstname': firstname, 'lastname':lastname,'email':email,'passwd':"",'id_default_group':group, 'id_odoo': idOdoo, 'associations': {'groups': {'group': [{'id':1},{'id':2},{'id':group}]} }}}
            print(apiPS.add('customers', data)['customer'])
            

class ProductCategory(models.Model):
    _name = "product.category"
    _inherit = "product.category"
    
    import re as reg
    
    def invioDatiPS(self, idOdoo, name,parent_id):
        apiPS = PrestashopApi('https://stage.planethoreca.it:443/api', 'A5WBAUB6TF2CRGCTR29HGAXMKQ19I4D4')
        link=name.lower()
        link=link.replace(" ","-")
        link=link.replace("/","-")
        
        if(parent_id!= -1):
            res=apiPS.get('categories/?filter[id_odoo]=['+str(parent_id)+']')
            
            if(dict(res)['categories'] is None):
                id_genitore=None 
            else:
                res=(dict(res['categories']['category']))
                id_genitore= res['@id']
                
        else:
            id_genitore=None
            
        res= apiPS.get('categories')
        name.encode(encoding='UTF-8',errors='strict')
        name=str(name)
        data = { 'category':{'active': 1,
                            'id_odoo' : idOdoo,
                            'name': {'language':{'@id':1,'#text':name}},
                            'link_rewrite': {'language':{'@id':1,'#text':link}},
                            'is_root_category':0,
                            'desc': None,
                            'meta_title':None,
                            'meta_description': None,
                            'meta_keywords': None,
                            'id_parent':id_genitore},}

        res = apiPS.add('categories', data)['category']
        
        
class ProductTemplate(models.Model):
    _name = "product.template"
    _inherit = "product.template"
    
    import re as reg
    
    def invioDatiPS(self, idOdoo, name, categ, idsCategorie, price, riferimento, tasse, barcode, peso, unita):
        apiPS = PrestashopApi('https://stage.planethoreca.it:443/api', 'A5WBAUB6TF2CRGCTR29HGAXMKQ19I4D4')
        link_rewrite = name.lower()  #link_rewrite
        link_rewrite = link_rewrite.replace(" ", "-")
        link_rewrite = link_rewrite.replace(".", "-")
        link_rewrite = link_rewrite.replace("ò", "o")
        link_rewrite = link_rewrite.replace("à", "a")
        link_rewrite = link_rewrite.replace("è", "e")
        link_rewrite = link_rewrite.replace("é", "e")
        link_rewrite = link_rewrite.replace("'", "")
        link_rewrite = link_rewrite.replace("ì", "i")
        link_rewrite = link_rewrite.replace("ù", "u")
        
        tasse=str(tasse)
        _logger.info(tasse)
        if(tasse.find('22') !=-1):
            tasse=1
        elif(tasse.find('10') !=-1):
            tasse=2
        elif(tasse.find('4')!=-1):
            tasse=4
        elif(tasse.find('5')!=-1):
            tasse=9
        elif(tasse.find('E11') !=-1):
            tasse=7
        else:
            tasse=1
        
        res=apiPS.get('categories/?filter[id_odoo]=['+str(categ)+']')
        
        
        if(dict(res)['categories'] is None):
            categ=0
        else:
            res=(dict(res['categories']['category']))
            categ= res['@id']
            
        
        
        res= apiPS.get('products/?filter[id_odoo]=['+str(idOdoo)+']')

        if(dict(res)['products'] is None):

            data = {'product': {'active': 1,
                                'name': {'language':{'@id':1,'#text':name}},
                                'price':price,
                                'id_category_default': categ,
                                'categories': {'category':{'id': categ}},
                                'id_odoo': idOdoo,
                                'link_rewrite':{'language':{'@id':1,'#text':link_rewrite}},
                                'id_tax_rules_group' : tasse,
                                'ean13': barcode,
                                'weight': peso,
                                'desc': None,
                                'desc_short':None,
                                'meta_title':None,
                                'meta_description':None,
                                'meta_keywords':None,
                                'reference':riferimento,
                                }}
            apiPS.add('products', data)

        else:
            res=(dict(res['products']['product']))
            id_presta= res['@id']

            data = {'product': {'id':id_presta,
                                'active': 1,
                                'name': {'language':{'@id':1,'#text':name}},
                                'price':price,
                                'id_category_default': categ,
                                'categories': {'category':{'id': categ}},
                                'id_odoo': idOdoo,
                                'link_rewrite':{'language':{'@id':1,'#text':link_rewrite}},
                                'id_tax_rules_group' : tasse,
                                'ean13': barcode,
                                'weight': peso,
                                'desc': None,
                                'desc_short':None,
                                'meta_title':None,
                                'meta_description':None,
                                'meta_keywords':None,
                                'reference':riferimento,
                                }}

            apiPS.edit('products/'+id_presta, data)
            
        
class StockQuant(models.Model):
    _name = "stock.quant"
    _inherit = "stock.quant"
    
    import re as reg
    def invioDatiPS(self, idOdoo, qty):
        apiPS = PrestashopApi('https://stage.planethoreca.it:443/api', 'A5WBAUB6TF2CRGCTR29HGAXMKQ19I4D4')
        
        res= apiPS.get('products/?filter[id_odoo]=['+str(idOdoo)+']')
        res=(dict(res['products']['product']))
        id_presta= res['@id']

        id_quantity= apiPS.get('stock_availables/?filter[id_product]=['+str(id_presta)+']')
        id_quantity=dict(id_quantity['stock_availables']['stock_available'])
        id_quantity= id_quantity['@id']

        data = {'stock_available': {'id':int(id_quantity),
                        'id_product':int(id_presta),
                        'id_product_attribute':0,
                        'id_shop': 1,
                        'id_shop_group':0,
                        'quantity': int(qty),
                        'id_odoo': idOdoo,
                        'depends_on_stock':0,
                        'out_of_stock':0,
                        }}
        apiPS.edit('stock_availables/', data)