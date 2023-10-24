from django.test import TestCase
from rest_framework.test import APIClient
from app.models import Item

class ItemAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item = Item.objects.create(name="Test Item", description="This is a test item")

    def test_get_item(self):
        response = self.client.get(f"/api/items/{self.item.id}/")
        self.assertEqual(response.status_code, 200)

    def test_get_nonexistent_item(self):
        response = self.client.get("/api/items/999/")
        self.assertEqual(response.status_code, 404)

    def test_create_item(self):
        data = {'name': 'New Item', 'description': 'A new item'}
        response = self.client.post("/api/items/", data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Item.objects.count(), 2)