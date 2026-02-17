# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details
from re import search

from dateutil.relativedelta import relativedelta
from datetime import date

from docutils.utils.smartquotes import stupefyEntities
from openpyxl.styles.builtins import total

from odoo import models, fields
from odoo.addons.test_import_export.models.models_export_impex import name, selection_fn
from odoo.odoo import api
from odoo.exceptions import ValidationError


class Student(models.Model):
    """
    Student Model: Handles student's profile and their relationships
                   with teacher and class. Contains auto compute age function
                   and onchange functionality
    """
    _name = "school.student"
    _description = "student table"

    # -------------------------------------------------------------------------
    # FIELDS
    # -------------------------------------------------------------------------
    user_id = fields.Many2one('res.users', string="Related User")

    name = fields.Char(string='Student Name')
    student_id = fields.Char(string='Student ID')
    enrollment_number = fields.Integer(string='Enrollment')

    class_id = fields.Many2one('school.classes', string="Class Name")
    location = fields.Text(string='Location')  # used Text field here just because the address can be long
    total_marks = fields.Float(string='Total Marks')
    gender = fields.Char(string="Gender")
    gender_type = fields.Selection([('Male', 'M'), ('Female', 'F')], string="Gender Type", store=True)
    teacher_id = fields.Many2many('school.teacher', string="Teacher")
    favoirate_teachers = fields.Many2one('school.teacher', string="Favoirate Teacher")
    dob = fields.Date(string="DOB")
    age = fields.Integer(string="Age", compute="_compute_age", store=True)

    # -------------------------------------------------------------------------
    # COMPUTE METHODS
    # -------------------------------------------------------------------------
    @api.depends('dob')
    def _compute_age(self):
        self.age = False
        for res in self:
            res.age = relativedelta(date.today(), res.dob).years  # it will give Integer value in year format

    # -------------------------------------------------------------------------
    # ONCHANGE METHODS
    # -------------------------------------------------------------------------
    @api.onchange('gender')
    def _onchange_grade(self):
        if self.gender == 'Male':
            self.gender_type = 'Male'
        elif self.gender == 'Female':
            self.gender_type = 'Female'
        else:
            self.gender_type = False

    # -------------------------------------------------------------------------
    # ACTION
    # -------------------------------------------------------------------------
    def search_names(self):
        # domain = ['&',('gender', '=', 'Female'),('age','>','10')]
        students = self.search([
            ('gender', '=', 'Female'), ('age', '>', '10')
        ])
        for s in students:
            print(s.name)

    def read_favoirate_teachers(self):
        fav_teacher = self.read(['favoirate_teachers'])
        for t in fav_teacher:
            print(t)

    # if i want to get the data where the student are above age 15
    def eligible_for_sports(self):
        sport_student = self.search_read(
            [('age', '>', '15')],  # domain
            ['name', 'age', 'gender']  # fields
        )
        for data in sport_student:
            print(data)