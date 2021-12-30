# -*- coding: utf-8 -*-
# from odoo import http


# class AbcCampiMancanti(http.Controller):
#     @http.route('/abc_campi_mancanti/abc_campi_mancanti/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_campi_mancanti/abc_campi_mancanti/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_campi_mancanti.listing', {
#             'root': '/abc_campi_mancanti/abc_campi_mancanti',
#             'objects': http.request.env['abc_campi_mancanti.abc_campi_mancanti'].search([]),
#         })

#     @http.route('/abc_campi_mancanti/abc_campi_mancanti/objects/<model("abc_campi_mancanti.abc_campi_mancanti"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_campi_mancanti.object', {
#             'object': obj
#         })
