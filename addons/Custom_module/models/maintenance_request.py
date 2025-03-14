from odoo import models, fields, api, _
from odoo.exceptions import UserError

class MaintenanceRequest(models.Model):
    _inherit = 'maintenance.request'
    
    stock_confirmed = fields.Boolean(string='Xác nhận trong kho', default=False)

    def action_check_inventory(self):
        for request in self:
            if request.equipment_id and request.equipment_id.stock_quant_ids.filtered(lambda q: q.quantity > 0):
                request.write({'state': 'waiting_approval', 'message': _('Thiết bị có trong kho, chờ duyệt.')})
                request.write({'stage_id': self.env.ref('maintenance.stage_confirmed').id})
            else:
                raise UserError(_('Thiết bị không có trong kho, không thể thực hiện đơn.'))

    def action_approve(self):
        self.write({'stage_id': self.env.ref('maintenance.stage_approved').id})

    def action_reject(self):
        self.write({'stage_id': self.env.ref('maintenance.stage_rejected').id})
