from odoo import models, fields, api

class BreakSession(models.Model):
    _name = 'break.session'
    _description = 'Work/Break Session Log'

    start_time = fields.Datetime(string="Start Time", required=True)
    end_time = fields.Datetime(string="End Time")
    is_break = fields.Boolean(string="Is Break", default=False)
    duration = fields.Float(string="Duration (minutes)", compute="_compute_duration", store=True)

    @api.depends('start_time', 'end_time')
    def _compute_duration(self):
        for rec in self:
            if rec.start_time and rec.end_time:
                delta = rec.end_time - rec.start_time
                rec.duration = delta.total_seconds() / 60
            else:
                rec.duration = 0.0

class BreakConfig(models.Model):
    _name = 'break.config'
    _description = 'Break Timer Configuration'

    name = fields.Char(default="Default Config")
    work_interval = fields.Integer(string="Work Duration (minutes)", default=25)
    break_interval = fields.Integer(string="Break Duration (minutes)", default=5)
    auto_restart = fields.Boolean(string="Auto Restart Session", default=True)

class BreakReport(models.Model):
    _name = 'break.report'
    _description = 'Break/Work Time Report'

    date = fields.Date(default=fields.Date.today)
    total_work = fields.Float(string="Total Work (min)")
    total_break = fields.Float(string="Total Break (min)")
    session_ids = fields.One2many('break.session', 'report_id', string="Sessions")
