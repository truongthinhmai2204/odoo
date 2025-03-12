from odoo import models, fields, api, _
from odoo.exceptions import UserError

class EquipmentConfirmation(models.Model):
    _name = 'equipment.confirmation'
    _description = 'Equipment Confirmation'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # Cho phép theo dõi thông tin trên chatter

    name = fields.Char(string="Confirmation Reference", required=True, copy=False, readonly=True, default=lambda self: _('New'))
    equipment_id = fields.Many2one('maintenance.equipment', string="Equipment", required=True)
    user_id = fields.Many2one('res.users', string="Confirmed By", default=lambda self: self.env.user, readonly=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('rejected', 'Rejected')
    ], string="Status", default='draft', tracking=True)

    note = fields.Text(string="Notes")

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('equipment.confirmation') or _('New')
        return super(EquipmentConfirmation, self).create(vals)

    def action_confirm(self):
        """Xác nhận thiết bị"""
        for record in self:
            if record.state != 'draft':
                raise UserError(_("Only draft records can be confirmed."))
            record.state = 'confirmed'

    def action_reject(self):
        """Từ chối xác nhận thiết bị"""
        for record in self:
            if record.state != 'draft':
                raise UserError(_("Only draft records can be rejected."))
            record.state = 'rejected'
