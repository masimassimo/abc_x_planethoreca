# -*- coding: utf-8 -*-
# from odoo import http


# class AbcPosText(http.Controller):
#     @http.route('/abc_pos_text/abc_pos_text/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_pos_text/abc_pos_text/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_pos_text.listing', {
#             'root': '/abc_pos_text/abc_pos_text',
#             'objects': http.request.env['abc_pos_text.abc_pos_text'].search([]),
#         })

#     @http.route('/abc_pos_text/abc_pos_text/objects/<model("abc_pos_text.abc_pos_text"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_pos_text.object', {
#             'object': obj
#         })
