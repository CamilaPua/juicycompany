from django.test import TestCase, Client
from .models import User

class PurchaseViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client = Client()
        self.client.login(username='testuser', password='password123')

    def test_purchase_view(self):
        response = self.client.get('/juiceapp/purchase/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'User ID: {}'.format(self.user.id))
        self.assertContains(response, 'User name: testuser')
    
    def test_purchase_view_logedout(self):
        self.client.logout()
        response = self.client.get('/juiceapp/purchase/')
        self.assertEqual(response.status_code, 302)