# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details
from odoo import models, fields


class Teacher(models.Model):
    """
        Teacher Model: Handles teacher's profile and their relationships
                        with subjects and students.
    """
    _name = "school.teacher"
    _description = "Teacher table"

    # -------------------------------------------------------------------------
    # FIELDS
    # -------------------------------------------------------------------------
    user_id = fields.Many2one('res.users', string="Related User")

    name = fields.Char(string='Name')
    employee_id = fields.Char(string='Employee ID')
    subject = fields.Many2many('school.subject', string='Subject')
    email = fields.Char(string="Email")
    joining_date = fields.Date(string="Joining Date", default=fields.Date.today)

    student_ids = fields.Many2many('school.student', string="Students")
    student_lists = fields.One2many('school.student', 'favoirate_teachers', string="student_list")
