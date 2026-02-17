# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details
from odoo import models, fields


class Classes(models.Model):
    """
        Classes Model: Acts as a central hub to manage different school grades/sections.
                       It links specific subjects and a list of enrolled students to a single class.
    """

    _name = "school.classes"
    _description = "Class for student"

    # -------------------------------------------------------------------------
    # FIELDS
    # -------------------------------------------------------------------------
    name = fields.Char(string="Class Name")
    subject_ids = fields.Many2many('school.subject', string="Subjects")
    student_ids = fields.One2many('school.student', 'class_id', string='Students')
