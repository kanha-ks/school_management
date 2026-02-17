# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details
from odoo import models, fields


class Subjects(models.Model):
    """
    Subject Model: Handles subject's profile and their relationships
                   with class model.
    """
    _name = "school.subject"
    _description = "Subjects in school"

    # -------------------------------------------------------------------------
    # FIELDS
    # -------------------------------------------------------------------------
    name = fields.Char(string="Subject")
    class_name = fields.Many2many('school.classes', string="Class")
