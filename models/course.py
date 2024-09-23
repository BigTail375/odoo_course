from odoo import models, fields

class Course(models.Model):
    _name = 'course.data'
    _description = 'Course Information'

    name = fields.Char(string='Course Name', required=True)
    description = fields.Text(string='Description')
    duration = fields.Integer(string='Duration (hours)')
    instructors = fields.Many2many('res.partner', string='Instructors')  # Linked to res.partner (contacts)
    price = fields.Float(string='Price', required=True)