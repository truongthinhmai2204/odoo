from odoo.tests.common import TransactionCase

class TestMaintenance(TransactionCase):

    def setUp(self):
        super().setUp()

        # Tạo thiết bị bảo trì trước
        self.equipment = self.env['maintenance.equipment'].create({
            'name': 'Test Equipment'
        })

        # Tạo yêu cầu bảo trì
        self.request = self.env['maintenance.request'].create({
            'name': 'Test Request',
            'equipment_id': self.equipment.id,
            'stage_id': self.env.ref('maintenance.stage_draft').id  # Đảm bảo có stage hợp lệ
        })

    def test_confirm_request(self):
        """Kiểm tra chuyển trạng thái khi xác nhận yêu cầu"""
        self.request.stage_id = self.env.ref('maintenance.stage_confirmed').id
        self.assertEqual(self.request.stage_id, self.env.ref('maintenance.stage_confirmed'))

    def test_reject_request(self):
        """Kiểm tra chuyển trạng thái khi từ chối yêu cầu"""
        self.request.stage_id = self.env.ref('maintenance.stage_cancelled').id
        self.assertEqual(self.request.stage_id, self.env.ref('maintenance.stage_cancelled'))
