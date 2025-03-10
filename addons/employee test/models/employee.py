from odoo import models, fields

class Employee(models.Model):
    _name = 'hr.employee'
    _description = 'Employee Record'

    name = fields.Char(string='Full Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    department = fields.Char(string='Department')
    hire_date = fields.Date(string='Hire Date')

    contract_ids = fields.One2many('hr.contract', 'employee_id', string='Contracts')
