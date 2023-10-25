from datetime import datetime

from rest_framework import status
from rest_framework.test import APITestCase

from habit_app.models import Habit
from users.models import User


class HabitCreateTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='testuser', password='test123password')
        self.habit = Habit.objects.create(
            user=self.user, place="Везде", time="10:00", action="Улыбнуться",
            is_pleasant=True, periodicity=1, time_to_complete=60, is_public=True
        )
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        """ Тест контроллера создания привычки """

        data = {
            "user": self.user.id, "place": "Везде", "time": datetime.strptime("10:00", "%H:%M").time(),
            "action": "Выпить стакан воды", "related_habit": self.habit.id, "periodicity": 1, "time_to_complete": 60,
            "is_public": True
        }

        response = self.client.post('/habit/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_habit_validation_error_1(self):
        """ Тест контроллера создания привычки (отработка валидатора №1) """

        data = {
            "user": self.user.id, "place": "Везде", "time": datetime.strptime("10:00", "%H:%M").time(),
            "action": "Выпить стакан воды", "periodicity": 1,
            "time_to_complete": 60, "is_public": True, "reward": "Почилить", "is_pleasant": True
        }

        response = self.client.post('/habit/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(),
                         {'non_field_errors': ['У приятной привычки не может быть вознаграждения!']})

    def test_create_habit_validation_error_2(self):
        """ Тест контроллера создания привычки (отработка валидатора №2) """

        data = {
            "user": self.user.id, "place": "Везде", "time": datetime.strptime("10:00", "%H:%M").time(),
            "action": "Выпить стакан воды", "related_habit": self.habit.id, "periodicity": 1,
            "time_to_complete": 60, "is_public": True, "is_pleasant": True
        }

        response = self.client.post('/habit/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(),
                         {'non_field_errors': ['У приятной привычки не может быть связанной привычки!']})

    def test_create_habit_validation_error_3(self):
        """ Тест контроллера создания привычки (отработка валидатора №3) """

        data = {
            "user": self.user.id, "place": "Везде", "time": datetime.strptime("10:00", "%H:%M").time(),
            "action": "Выпить стакан воды", "related_habit": self.habit.id, "periodicity": 1, "reward": "Покурить",
            "time_to_complete": 60, "is_public": True
        }

        response = self.client.post('/habit/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(),
                         {'non_field_errors': ['Нельзя выбрать связанную привычку и вознаграждение одновременно!']})

    def test_create_habit_validation_error_4(self):
        """ Тест контроллера создания привычки (отработка валидатора '120 секунд') """

        data = {
            "user": self.user.id, "place": "Везде", "time": datetime.strptime("10:00", "%H:%M").time(),
            "action": "Выпить стакан воды", "related_habit": self.habit.id, "periodicity": 1,
            "time_to_complete": 130, "is_public": True
        }

        response = self.client.post('/habit/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(),
                         {'non_field_errors': ['Время выполнения привычки не должно превышать 120 секунд!']})

    def test_create_habit_validation_error_5(self):
        """ Тест контроллера создания привычки (отработка валидатора '7 дней') """

        data = {
            "user": self.user.id, "place": "Везде", "time": datetime.strptime("10:00", "%H:%M").time(),
            "action": "Выпить стакан воды", "related_habit": self.habit.id, "periodicity": 8,
            "time_to_complete": 110, "is_public": True
        }

        response = self.client.post('/habit/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(),
                         {'non_field_errors': ['Привычка должна выполняться не реже 1 раза в 7 дней!']})


class HabitListTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='testuser', password='test123password')
        self.habit = Habit.objects.create(
            user=self.user, place="Везде", time="10:00", action="Улыбнуться",
            is_pleasant=True, periodicity=1, time_to_complete=60, is_public=True
        )
        self.client.force_authenticate(user=self.user)

    def test_list_habit(self):
        """ Тест контроллера получения списка привычек """

        response = self.client.get('/habit/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class HabitPublicListTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='testuser', password='test123password')
        self.habit = Habit.objects.create(
            user=self.user, place="Везде", time="10:00", action="Улыбнуться",
            is_pleasant=True, periodicity=1, time_to_complete=60, is_public=True
        )
        self.client.force_authenticate(user=self.user)

    def test_list_public_habit(self):
        """ Тест контроллера получения списка публичных привычек """

        response = self.client.get('/public_habit/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class HabitUpdateTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='testuser', password='test123password')
        self.habit = Habit.objects.create(
            user=self.user, place="Везде", time="10:00", action="Улыбнуться",
            is_pleasant=True, periodicity=1, time_to_complete=60, is_public=True
        )
        self.client.force_authenticate(user=self.user)

    def test_update_habit(self):
        """ Тест контроллера редактирования привычки """

        data = {
            "user": self.user.id, "place": "Везде", "time": datetime.strptime("10:00", "%H:%M").time(),
            "action": "Выпить стакан воды", "related_habit": self.habit.id, "periodicity": 1, "time_to_complete": 60,
            "is_public": True
        }

        response = self.client.patch(f'/habit/update/{self.habit.id}/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class HabitRetrieveTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='testuser', password='test123password')
        self.habit = Habit.objects.create(
            user=self.user, place="Везде", time="10:00", action="Улыбнуться",
            is_pleasant=True, periodicity=1, time_to_complete=60, is_public=True
        )
        self.client.force_authenticate(user=self.user)

    def test_retrieve_habit(self):
        """ Тест контроллера отображения привычки по ее ID """

        response = self.client.get(f'/habit/{self.habit.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class HabitDeleteTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='testuser', password='test123password')
        self.habit = Habit.objects.create(
            user=self.user, place="Везде", time="10:00", action="Улыбнуться",
            is_pleasant=True, periodicity=1, time_to_complete=60, is_public=True
        )
        self.client.force_authenticate(user=self.user)

    def test_delete_habit(self):
        """ Тест контроллера удаления привычки по ее ID """

        response = self.client.delete(f'/habit/delete/{self.habit.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Habit.objects.filter(id=self.habit.id).exists())
