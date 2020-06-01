# -*- coding: utf-8 -*-
# from odoo import http


# class EmployeeIdSequenceYear(http.Controller):
#     @http.route('/employee_id_sequence_year/employee_id_sequence_year/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employee_id_sequence_year/employee_id_sequence_year/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('employee_id_sequence_year.listing', {
#             'root': '/employee_id_sequence_year/employee_id_sequence_year',
#             'objects': http.request.env['employee_id_sequence_year.employee_id_sequence_year'].search([]),
#         })

#     @http.route('/employee_id_sequence_year/employee_id_sequence_year/objects/<model("employee_id_sequence_year.employee_id_sequence_year"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employee_id_sequence_year.object', {
#             'object': obj
#         })
