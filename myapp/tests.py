from django.test import TestCase
from.models import Animal
from views import main
# Create your tests here.
class MyTestAnimal(TestCase):
    def setUp(self):
        Animal.objects.create(name = "lion", sound = "roar")
    def test_animals(self):
        lion = Animal.objects.get(name = "lion")
        

        self.assertEqual(lion.speak(), 'The lion says "roar"')

class MyTest(TestCase):
    def test_auto(self):
        
        self.assertEqual()