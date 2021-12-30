# -*- coding: utf-8 -*-
# from odoo import http


# class AbcCodiceArca(http.Controller):
#     @http.route('/abc_codice_arca/abc_codice_arca/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_codice_arca/abc_codice_arca/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_codice_arca.listing', {
#             'root': '/abc_codice_arca/abc_codice_arca',
#             'objects': http.request.env['abc_codice_arca.abc_codice_arca'].search([]),
#         })

#     @http.route('/abc_codice_arca/abc_codice_arca/objects/<model("abc_codice_arca.abc_codice_arca"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_codice_arca.object', {
#             'object': obj
#         })
