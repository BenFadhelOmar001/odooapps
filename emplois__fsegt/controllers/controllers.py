# -*- coding: utf-8 -*-
# from odoo import http


# class EmploisFsegt(http.Controller):
#     @http.route('/emplois__fsegt/emplois__fsegt/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/emplois__fsegt/emplois__fsegt/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('emplois__fsegt.listing', {
#             'root': '/emplois__fsegt/emplois__fsegt',
#             'objects': http.request.env['emplois__fsegt.emplois__fsegt'].search([]),
#         })

#     @http.route('/emplois__fsegt/emplois__fsegt/objects/<model("emplois__fsegt.emplois__fsegt"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('emplois__fsegt.object', {
#             'object': obj
#         })
