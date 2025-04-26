from odoo import models, fields
from odoo import api, fields, models, SUPERUSER_ID, _


class MaintenanceEquipmentCustom(models.Model):
    _name = 'maintenance.equipment.custom'
    _description = 'Maintenance Equipment Custom'

    name = fields.Char(string="Equipment Name", required=True)
    description = fields.Text(string="Description")
    category_id = fields.Many2one('maintenance.equipment.category.custom', string="Equipment Category Custom", ondelete="set null")
    technician_user_id = fields.Many2one('res.users', string='Technician', tracking=True)
    owner_user_id = fields.Many2one('res.users', string='Created by User', default=lambda s: s.env.uid)
    color = fields.Integer("Color Index", default=0)
    product_id = fields.Many2one('product.product', string='Related Product')
    employee_id = fields.Many2one('hr.employee', string="Employee")
    maintenance_team_id = fields.Many2one('maintenance.team.custom', string="Maintenance Team Custom")
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company, index=True)

    @api.model
    def _cron_generate_requests(self):
        """
            Generates maintenance request on the next_action_date or today if none exists
        """
        for equipment in self.search([('period', '>', 0)]):
            next_requests = self.env['maintenance.request.custom'].search([('stage_id.done', '=', False),
                                                    ('equipment_id', '=', equipment.id),
                                                    ('maintenance_type', '=', 'preventive'),
                                                    ('request_date', '=', equipment.next_action_date)])
            if not next_requests:
                equipment._create_new_request(equipment.next_action_date)

