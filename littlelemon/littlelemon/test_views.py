from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.views import *
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.create(Title="Dish1", Price=10, Inventory=50)
        Menu.objects.create(Title="Dish2", Price=15, Inventory=30)

    def test_getall(self):
        menuObjects = Menu.objects.all()
        serializer = MenuSerializer(menuObjects, many=True)
        client = APIClient()
        url = '/restaurant/menu/'
        response = client.get(url)

        self.assertEqual(response.data, serializer.data)
