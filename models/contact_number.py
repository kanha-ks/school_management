# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details
from odoo import models, fields


class Contact_Numbers(models.Model):
    """
        Contact Number showing the relationship between student contains the contact information
    """
    _name = "school.contact_numbers"
    _description = "Contact Number List"

    # -------------------------------------------------------------------------
    # FIELDS
    # -------------------------------------------------------------------------
    contact_number_id = fields.Char(string="Contact ID")
    contact_name = fields.Char(string="Name")
    contact_number = fields.Char(string="Mobile Number")
    # student_own_details = fields.Many2one('school.student', string="Student ID")
