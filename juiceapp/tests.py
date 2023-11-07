from django.test import TestCase, Client
from .models import User

class MyModelTestCase(TestCase):
    def test_create_user_and_print(self):
        user = User.objects.create_user(username="testuser", password="password123")
        print(f"User Name: {user.username}")
        print(f"User ID: {user.id}")
        self.assertEqual(user.username, "testuser")
        self.assertGreater(user.id, 0)

    def test_purchase_view(self):
        client = Client()
        client.login(username="testuser", password="password123")

        response = client.get('/juiceapp/purchase/')

        self.assertEqual(response.status_code, 200)