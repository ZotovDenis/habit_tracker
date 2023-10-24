from unittest import TestCase

from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser', password='test123password', chat_id=222222222222)

    def test_create_user(self):
        """ Тест контроллера создания пользователя """

        data = {
            "username": "test_user",
            "password": "test123password",
            "chat_id": 1222222222
        }

        response = self.client.post('/users/user/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), {"username": "test_user"})
        self.assertEqual(User.objects.all().count(), 2)

    def test_delete_user(self):
        """ Тест контроллера удаления пользователя """

        self.client.force_authenticate(user=self.user)

        response = self.client.delete(f'/users/user/delete/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateSuperuserTestCase(TestCase):
    def test_create_superuser(self):
        """ Тест функции создания superuser """

        if not User.objects.filter(username='admin').exists():

            User.objects.create_superuser(username='admin', email='admin@example.com', password='04102305')

        superuser = User.objects.get(username='admin')
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)
