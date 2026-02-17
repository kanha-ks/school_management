# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details
from odoo import models, fields


class SaleOrder(models.Model):
    """
        SaleOrder : A Model having the properties of Sale order model
                    it is inheriting the base model called : sale.order
    """

    _inherit = 'sale.order'

    # -------------------------------------------------------------------------
    # FIELDS
    # -------------------------------------------------------------------------
    student_id = fields.Many2one('school.student', string="Student")
    admission_no = fields.Char(string="Admission Number")
