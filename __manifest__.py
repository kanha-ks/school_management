# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details
{
    'name': 'School Management',
    'version': '1.0.0',
    'author': 'steve johns',
    'description': 'The school management system',
    'summary': 'The School Management System',
    'category': 'School',
    'depends': ['base', 'web', 'contacts', 'mail'],
    'data': [
        'data/server_action.xml',
        'security/school_groups.xml',
        'security/ir.model.access.csv',
        'security/school_management_rules_security.xml',
        'views/school_management_teacher_views.xml',
        'views/school_management_views.xml',
        'views/school_management_result_views.xml',
        'views/school_management_subject_views.xml',
        'views/school_management_class_views.xml',
        'views/school_management_menus.xml',
        'reports/student_report_template.xml',
    ],
    'sequence': 2,
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
}
