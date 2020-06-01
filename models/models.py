# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class employee_id_sequence_year(models.Model):
#     _name = 'employee_id_sequence_year.employee_id_sequence_year'
#     _description = 'employee_id_sequence_year.employee_id_sequence_year'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
