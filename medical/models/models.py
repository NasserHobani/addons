# -*- coding: utf-8 -*-

from odoo import models, fields, api


class medical(models.Model):
    _name = 'medical.medical'
    _description = 'medical.medical'

    name = fields.Char('name')
    code = fields.Char('Code')
    clinic_limit = fields.Integer('Clinic Limit')
    covid_vaccine = fields.Selection([('first', '1'), ('second', '2'), ('third', '3')], 'Covid Vaccine')
    employee = fields.Many2one('res.users','Employee')
    chair_from = fields.Integer('Chair From')
    chair_to = fields.Integer('Chair To')
