# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests
import ssl
from urllib3 import poolmanager
import json
import logging

_logger = logging.getLogger(__name__)


class abc_post_fatturapertutti(models.Model):
     _name = 'abc_post_fatturapertutti.abc_post_fatturapertutti'
     _description = 'abc_post_fatturapertutti.abc_post_fatturapertutti'
    
class TLSAdapter(requests.adapters.HTTPAdapter):
    

    def init_poolmanager(self, connections, maxsize, block=False):
        """Create and initialize the urllib3 PoolManager."""
        ctx = ssl.create_default_context()
        ctx.set_ciphers('DEFAULT@SECLEVEL=1')
        self.poolmanager = poolmanager.PoolManager(
                num_pools=connections,
                maxsize=maxsize,
                block=block,
                ssl_version=ssl.PROTOCOL_TLS,
                ssl_context=ctx)
        
class PosSession(models.Model):
    _inherit = 'pos.session'
    
    def inviaScontrinoAdEMiddleware(self, quantita, descrizione, prezzo, sconto, codiceIva):            
    
        dettaglioMidFormattato = {'quantità':quantita,'descrizione':descrizione, 'prezzo':prezzo, 'sconto':sconto, 'codiceIva':codiceIva}
        return dettaglioMidFormattato

    def inviaScontrinoAdE(self, oid, numeroRighe, dettaglioMidFormattato, contante, carta):            
        url = 'https://api.fatturapertutti.it/smartsale/8nysWpVo4kiJ4zeJObY80Q/Oceania990'
         
        if(carta==0):

            jsonPost = {"oid": oid,
                    "dettaglio": 
                    dettaglioMidFormattato,
                    "pagamentoContante": contante}
            
        elif(contante == 0):
            jsonPost = {"oid": oid,
                    "dettaglio": 
                    dettaglioMidFormattato,
                    "pagamentoElettronico": carta}
        else:
            jsonPost= {"oid": oid,
                    "dettaglio": 
                    dettaglioMidFormattato,
                    "pagamentoContante": contante,
                    "pagamentoElettronico": carta}
            
        jsonString = json.dumps(jsonPost, ensure_ascii=False)
        session = requests.session()
        session.mount('https://', TLSAdapter())
        res = session.post(url, data = jsonString.encode('utf-8'), headers={'Content-Type': 'text/plain; charset=utf-8'})
        _logger.info(jsonString)
        _logger.info(res.json())
        #responseFatturapertutti = json.dumps(res, ensure_ascii=False))
        #resLoad = json.loads(res.json())
        #_logger.info(type(res.json()))
        resJson = res.json()
        if(resJson['errorCode'] != 0):
            stringaErrore = "Qualcosa è andato storto! Contatta gli sviluppatori."
            return stringaErrore
        else:
            dataFatturapertutti = resJson['data']
            progressivo = resJson['progressivo']
            array = [dataFatturapertutti, progressivo]
            return array



    def cancellaScontrinoAdE(self, data, progressivo, totale):
        url = 'https://api.fatturapertutti.it/cancelsmartsale/8nysWpVo4kiJ4zeJObY80Q/Oceania990'
        
        jsonPost = {"progressivo": progressivo,
                    "data": data,
                    "totale": totale}
        
        jsonString = json.dumps(jsonPost, ensure_ascii=False)
        session = requests.session()
        session.mount('https://', TLSAdapter())
        res = session.post(url, data = jsonString.encode('utf-8'), headers={'Content-Type': 'text/plain; charset=utf-8'})
        _logger.info(jsonString)
        _logger.info(res.json())
        #responseFatturapertutti = json.dumps(res, ensure_ascii=False))
        #resLoad = json.loads(res.json())
        _logger.info(type(res.json()))
        resJson = res.json()
        if(resJson['errorCode'] != 0):
            stringaErrore = "Qualcosa è andato storto! Contatta gli sviluppatori."
            return stringaErrore
        else:
            return str(resJson)



            
    

        
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
