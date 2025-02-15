# -*- coding: utf-8 -*-
# from odoo import http


# class ItProcurement(http.Controller):
#     @http.route('/it_procurement/it_procurement', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/it_procurement/it_procurement/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('it_procurement.listing', {
#             'root': '/it_procurement/it_procurement',
#             'objects': http.request.env['it_procurement.it_procurement'].search([]),
#         })

#     @http.route('/it_procurement/it_procurement/objects/<model("it_procurement.it_procurement"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('it_procurement.object', {
#             'object': obj
#         })

