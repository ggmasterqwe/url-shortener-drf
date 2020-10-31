from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAppModelTest(TestCase):
    def test_createing_user(self):
        data ={
            'username': 'test_user',
            'password': 'testpassword',
            'email': 'test@mail.com'
        }

        user = User.objects.create(**data)        

        self.assertEqual(user, User.objects.get(**data))
