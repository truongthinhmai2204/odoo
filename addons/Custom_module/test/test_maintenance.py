from odoo.tests.common import TransactionCase

class TestMaintenance(TransactionCase):
    def setUp(self):
        super().setUp()
        self.request = self.env['maintenance.request'].create({
            'name': 'Test Request',
            'equipment_id': self.env['maintenance.equipment'].create({'name': 'Test Equipment'}).id,
            'state': 'draft'
        })

    def test_confirm_request(self):
        self.request.action_confirm_request()
        self.assertEqual(self.request.state, 'waiting_approval')

    def test_reject_request(self):
        self.request.action_reject_request()
        self.assertEqual(self.request.state, 'rejected')
