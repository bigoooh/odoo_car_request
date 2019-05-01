# -*- coding: utf-8 -*-
from odoo import http

# class CarRequest(http.Controller):
#     @http.route('/car_request/car_request/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/car_request/car_request/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('car_request.listing', {
#             'root': '/car_request/car_request',
#             'objects': http.request.env['car_request.car_request'].search([]),
#         })

#     @http.route('/car_request/car_request/objects/<model("car_request.car_request"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('car_request.object', {
#             'object': obj
#         })