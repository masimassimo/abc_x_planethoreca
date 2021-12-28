# -*- coding: utf-8 -*-
# from odoo import http


# class AbcPostFatturapertutti(http.Controller):
#     @http.route('/abc_post_fatturapertutti/abc_post_fatturapertutti/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_post_fatturapertutti/abc_post_fatturapertutti/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_post_fatturapertutti.listing', {
#             'root': '/abc_post_fatturapertutti/abc_post_fatturapertutti',
#             'objects': http.request.env['abc_post_fatturapertutti.abc_post_fatturapertutti'].search([]),
#         })

#     @http.route('/abc_post_fatturapertutti/abc_post_fatturapertutti/objects/<model("abc_post_fatturapertutti.abc_post_fatturapertutti"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_post_fatturapertutti.object', {
#             'object': obj
#         })
