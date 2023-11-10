from django.test import TestCase, Client
from .models import *

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
        url_in_test = response.url
        self.assertEqual(url_in_test, "/juiceapp/login/?next=/juiceapp/purchase/")

    def test_append_juices(self):
        
        juice_data = [

            {"name": "Jugo de naranja", "price": 5000},
            {"name": "Jugo de manzana", "price": 4000},
            {"name": "Jugo de piña", "price": 6000},
            
            ]
        
        for data in juice_data:
            jugo = Juice(**data)
            jugo.save()

        for juice_db, juice_data in zip(Juice.objects.all(), juice_data):
            self.assertEqual(juice_db.name, juice_data["name"])
            self.assertEqual(juice_db.price, juice_data["price"])
