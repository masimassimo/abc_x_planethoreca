# -*- coding: utf-8 -*-
# from odoo import http


# class AbcCodiceIva(http.Controller):
#     @http.route('/abc_codice_iva/abc_codice_iva/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_codice_iva/abc_codice_iva/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_codice_iva.listing', {
#             'root': '/abc_codice_iva/abc_codice_iva',
#             'objects': http.request.env['abc_codice_iva.abc_codice_iva'].search([]),
#         })

#     @http.route('/abc_codice_iva/abc_codice_iva/objects/<model("abc_codice_iva.abc_codice_iva"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_codice_iva.object', {
#             'object': obj
#         })
