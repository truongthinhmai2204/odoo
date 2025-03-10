from odoo import models, fields

class Contract(models.Model):
    _name = 'hr.contract.custom'
    _description = 'Employee Contract'

    employee_id = fields.Many2one('hr.employee.custom', string='Employee', required=True)
    salary = fields.Float(string='Salary')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')

    status = fields.Selection([
        ('active', 'Active'),
        ('expired', 'Expired'),
    ], string='Status', default='active')
