from odoo import fields, models
from odoo.odoo.orm.decorators import ondelete


class Exams(models.Model):

    # it should contains student name , student subject , student marks
    _name = 'school.exams'
    _description = 'Student Exam Model'

    name = fields.Char(string="Exam ")

    student_id = fields.Many2one(
        'school.student',
        string="Student",
        ondelete="cascade"
    )

    subject_id = fields.Many2one(
        'school.subject',
         string="Subject",
         ondelete="cascade"
    )

    marks = fields.Float(string="Marks")


