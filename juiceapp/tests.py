from django.test import TestCase
from .models import User

class MyModelTestCase(TestCase):
    def test_create_user_and_print(self):
        user = User.objects.create_user(username="testuser", password="password123")
        print(f"User Name: {user.username}")
        print(f"User ID: {user.id}")
        self.assertEqual(user.username, "testuser")
        self.assertGreater(user.id, 0)