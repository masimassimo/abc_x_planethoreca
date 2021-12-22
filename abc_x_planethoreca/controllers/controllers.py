# -*- coding: utf-8 -*-
# from odoo import http


# class AbcXPlanethoreca(http.Controller):
#     @http.route('/abc_x_planethoreca/abc_x_planethoreca/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_x_planethoreca/abc_x_planethoreca/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_x_planethoreca.listing', {
#             'root': '/abc_x_planethoreca/abc_x_planethoreca',
#             'objects': http.request.env['abc_x_planethoreca.abc_x_planethoreca'].search([]),
#         })

#     @http.route('/abc_x_planethoreca/abc_x_planethoreca/objects/<model("abc_x_planethoreca.abc_x_planethoreca"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_x_planethoreca.object', {
#             'object': obj
#         })
