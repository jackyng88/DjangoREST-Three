import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from profiles.api.serializers import ProfileSerializer
from profiles.models import Profile


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {
            'username': 'testuser',
            'email': 'test@testemail.com',
            'password1': 'somepassword1',
            'password2': 'somepassword1'
        }

        response = self.client.post('/api/rest-auth/registration/', data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ProfileViewSetTestCase(APITestCase):

    list_url = reverse('profile-list')

    def setUp(self):
        self.user = User.objects.create_user(username='luffy',
                                             password='onepiece123')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_profile_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_profile_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_profile_detail_retrieve(self):
        response = self.client.get(reverse('profile-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user'], 'luffy')

    def test_profile_update_by_owner(self):
        response = self.client.put(reverse('profile-detail', kwargs={'pk': 1}),
                                    {'city': 'East Blue', 'bio':'Pirate King'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), 
                         {'id': 1, 'user': 'luffy', 'bio': 'Pirate King',
                          'city': 'East Blue', 'avatar': None})

    def test_profile_update_by_random_user(self):
        random_user = User.objects.create_user(username='random', 
                                               password='password123123')
        self.client.force_authenticate(user=random_user)
        response = self.client.put(reverse('profile-detail', kwargs={'pk': 1}),
                                    {'bio':'huehuehue'})

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        
        




