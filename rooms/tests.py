from django.test import TestCase
from .models import Room

class RoomModelTest(TestCase):

    def test_create_room(self):
        room = Room.objects.create(
            room_number='101',
            room_type='Single',
            price=100.00,
            is_available=True
        )
        self.assertEqual(room.room_number, '101')
        self.assertEqual(room.room_type, 'Single')
        self.assertEqual(room.price, 100.00)
        self.assertTrue(room.is_available)

    def test_room_str_method(self):
        room = Room.objects.create(
            room_number='101',
            room_type='Single',
            price=100.00,
            is_available=True
        )
        self.assertEqual(str(room), '101')  # Assuming __str__ method returns room_number
