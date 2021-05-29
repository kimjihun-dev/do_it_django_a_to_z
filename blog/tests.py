from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post


# Create your tests here.
class TestView(TestCase):
    def setUp(self):
        self.Client = Client

    def test_create_post(self):
        response = self.client.get('/blog/crate_post')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')

        self.assertEqual('Create Post - Blog', soup.title.text)
        main_area = soup.find('div', id='main-area')
        self.assertEqual('Create New Post', main_area.text)
