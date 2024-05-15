from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test_user', email='test@example.com', password='test_password')

    def test_signup(self):
        data = {'username': 'new_user', 'password': 'new_password', 'email': 'new_user@example.com'}
        response = self.client.post('/api/signup/', data, format='json')  # Adicione uma barra inicial para o caminho completo
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login(self):
        data = {'username': 'test_user', 'password': 'test_password'}
        response = self.client.post('/api/login/', data, format='json')  # Adicione uma barra inicial para o caminho completo
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_test_token(self):
        self.client.login(username='test_user', password='test_password')
        response = self.client.get('/api/test_token/')  # Adicione uma barra inicial para o caminho completo
        self.assertEqual(response.status_code, status.HTTP_200_OK)
