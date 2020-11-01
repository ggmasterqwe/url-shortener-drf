from django.test import TestCase
from UrlShortenerApp.urls.models import Url
from django.contrib.auth import get_user_model

User = get_user_model()

class UrlsModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@mail.com',
                                        password='testpassword')

    def test_create_url_with_slug(self):
        data = {
            'user':self.user,
            'user_url': 'www.github.com/ggmasterqwe/url-shorter-drf',
            'slug':'urksa'
        }

        url = Url.objects.create(**data)

        self.assertAlmostEqual(url, Url.objects.get(**data))

    def test_create_url_without_slug(self):
        data = {
            'user':self.user,
            'user_url': 'www.github.com/ggmasterqwe/url-shorter-drf',
        }

        url = Url.objects.create(**data)
        data['slug'] = url.slug
        self.assertAlmostEqual(url, Url.objects.get(**data))