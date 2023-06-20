from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import MenuItem
from .serializers import MenuSerializer

# Create your tests here.

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item.price, 80)


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_items = [
            MenuItem.objects.create(title='Item 1', price=10.99, inventory=5),
            MenuItem.objects.create(title='Item 2', price=15.99, inventory=10),
            MenuItem.objects.create(title='Item 3', price=8.99, inventory=3),
        ]

    def test_getall(self):
        url = reverse('menu') 

        response = self.client.get(url)
        menu_data = MenuItem.objects.all()
        serializer = MenuSerializer(menu_data, many=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)