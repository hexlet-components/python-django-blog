from django.test import TestCase
from django.urls import reverse


class AppTest(TestCase):

    def test_index_page(self):
        response = self.client.get(reverse('root'))
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
