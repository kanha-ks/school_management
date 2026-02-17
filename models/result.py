# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details
from odoo import models, fields


class Result(models.Model):
    """
    Result : Manages student examination scores, grade calculations,
             and links students with their respective teachers and subjects.
    """
    _name = "school.result"
    _description = "Student results"

    # -------------------------------------------------------------------------
    # FIELDS
    # -------------------------------------------------------------------------
    name = fields.Char(string="Student Name")
    marks = fields.Float(string="Marks")
    status = fields.Boolean("Pass", default=False)
