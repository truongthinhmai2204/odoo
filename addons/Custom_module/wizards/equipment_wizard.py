from odoo import models, fields, api

class EquipmentWizard(models.TransientModel):
    _name = 'equipment.wizard'
    _description = 'Equipment Confirmation Wizard'

    equipment_id = fields.Many2one('equipment.confirmation', string="Thiết bị")
    confirm_note = fields.Text(string="Ghi chú xác nhận")

    def confirm_equipment(self):
        self.equipment_id.status = 'confirmed'
