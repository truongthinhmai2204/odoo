from odoo import models, fields, api

class BreakSession(models.Model):
    _name = 'break.session'
    _description = 'Work/Break Session Log'

    start_time = fields.Datetime(string="Start Time", required=True)
    end_time = fields.Datetime(string="End Time")
    is_break = fields.Boolean(string="Is Break", default=False)
    duration = fields.Float(string="Duration (minutes)", compute="_compute_duration", store=True)
    report_id = fields.Many2one('break.report', string="Report")

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

    name = fields.Char(string="Name")
    work_duration = fields.Integer(string="Work Duration")
    break_duration = fields.Integer(string="Break Duration")
    repeat_count = fields.Integer(string="Repeat Count")
    report_id = fields.Many2one('break.report', string="Report")

class BreakReport(models.Model):
    _name = 'break.report'
    _description = 'Break/Work Time Report'

    date = fields.Date(default=fields.Date.today)
    total_work = fields.Float(string="Total Work (min)")
    total_break = fields.Float(string="Total Break (min)")
    session_ids = fields.One2many('break.session', 'report_id', string="Sessions")
    config_ids = fields.One2many('break.config', 'report_id', string="Configurations") 
