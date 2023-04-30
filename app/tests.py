from django.test import TestCase
from django.urls import reverse


class TestProductCount(TestCase):
    url = reverse("product_count")

    def test(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"product_count": 28066})


class TestProductNames(TestCase):
    url = reverse("product_list")

    def test(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json().get("product_names")), 28066)


class TestProductNamesWithSpareParts(TestCase):
    url = reverse("spare_parts_list")

    def test(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json().get("products_with_spare_parts")), 28066)
