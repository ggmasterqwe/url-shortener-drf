from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from UrlShortenerApp.urls import apis
from UrlShortenerApp.urls.models import Url


User = get_user_model()


class URLApisTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='testemail@mail.com', password ='password')
    

    def test_create_url_test(self):
        url =  reverse('add-url')
        data = {
            'user_url': 'http://www.google.com',
            'slug': 'test',
            
        }
        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data, 'json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Url.objects.count(), 1)
        self.assertEqual(response.data, dict(data,user=self.user.id))


