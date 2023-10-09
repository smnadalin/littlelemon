from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="Icecream", Price=80, Inventory=100)
        self.assertEqual(str(item), "Icecream : 80")