# -*- coding: utf-8 -*-

from odoo import models, fields, api
import random
import numpy as np
from odoo.exceptions import UserError
from datetime import datetime


class medical(models.Model):
    _name = 'medical.clinic_settings'
    _description = 'medical.medical'

    name = fields.Char('name')
    code = fields.Char('Code')
    clinic_limit = fields.Integer('Clinic Limit')
    vaccine = fields.Many2many('medical.vaccine_settings', 'vaccine_clinic_rel', 'vaccine')
    employee_id = fields.Many2one('res.users', 'Employee')
    chair_from = fields.Integer('Chair From')
    chair_to = fields.Integer('Chair To')


class patient(models.Model):
    _name = 'medical.patient'
    _description = 'medical.medical'

    name = fields.Char('name')
    status = fields.Selection([('waiting', 'Waiting'), ('clinic', 'Clinic'), ('done', 'Done')], "status")
    login = fields.Datetime('Login', store=True, compute='status_d')
    in_the_clinic = fields.Datetime('Clinic', store=True, compute='status_d')
    finish = fields.Datetime('Finish', store=True, compute='status_d')
    active = fields.Boolean('Active')
    # vaccine = fields.Boolean('vaccine')
    covid_vaccine = fields.Many2one('medical.vaccine_settings', 'Covid Vaccine')
    clinic_id = fields.Many2one('medical.clinic_settings', 'Medical')
    employee_id = fields.Many2one('res.users', 'Employee', related='clinic_id.employee_id', readonly=True)
    chair_number = fields.Integer('chair_number')

    def find_chair(self):
        for record in self:
            if record.clinic_id.chair_to and record.clinic_id.chair_from:
                range = random.randrange(record.clinic_id.chair_to, record.clinic_id.chair_from)

                for limit in range:
                    count = record.env['medical.patient'].search_count(
                        [('active', '=', True), ('clinic_id', '=', record.clinic_id.id), ('chair_number', '=', limit)])
                    if count == 0:
                        record.chair_number = limit

    @api.onchange("clinic_id")
    def check_if_clinic_not_full(self):
        for record in self:
            if record.clinic_id and record.clinic_id.clinic_limit:
                count = record.env['medical.patient'].search_count(
                    [('active', '=', True), ('clinic_id', '=', record.clinic_id.id)])
                if count >= record.clinic_id.clinic_limit:
                    raise UserError("العيادة ممتلئة")

    @api.depends('status')
    def status_d(self):
        if self.status:
            if self.status in ['waiting']:
                self.login = datetime.now()
            if self.status in ['clinic']:
                self.in_the_clinic = datetime.now()
            if self.status in ['done']:
                self.finish = datetime.now()


class vaccine_type(models.Model):
    _name = 'medical.vaccine_type_settings'
    _description = 'medical.medical'

    name = fields.Char("Name")


class vaccine(models.Model):
    _name = 'medical.vaccine_settings'
    _description = 'medical.medical'

    type_id = fields.Many2one('medical.vaccine_type_settings', 'Type')
    name = fields.Char('name', store=True, compute='type',readonly=False)

    @api.depends('type_id')
    def type(self):
        if self.type_id:
            self.name = self.type_id.name
