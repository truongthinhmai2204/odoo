from odoo.tests.common import TransactionCase

class TestEquipment(TransactionCase):

    def setUp(self):
        super().setUp()
        self.equipment = self.env['equipment.confirmation'].create({
            'name': 'Laptop Test',
            'status': 'pending'
        })

    def test_equipment_confirmation(self):
        self.equipment.status = 'confirmed'
        self.assertEqual(self.equipment.status, 'confirmed', "Trạng thái không đúng!")
