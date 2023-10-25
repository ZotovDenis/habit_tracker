from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    """ Модель Привычки"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель привычки', **NULLABLE)
    place = models.CharField(max_length=60, verbose_name='Место привычки')
    time = models.TimeField(verbose_name='Время выполнения')
    action = models.CharField(max_length=100, verbose_name='Действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    related_habit = models.ForeignKey('Habit', on_delete=models.SET_NULL, verbose_name='Связанная привычка', **NULLABLE)
    periodicity = models.PositiveIntegerField(default=1, verbose_name='Периодичность выполнения')
    reward = models.CharField(max_length=100, verbose_name='Вознаграждение за выполнение', **NULLABLE)
    time_to_complete = models.SmallIntegerField(verbose_name='Время на выполнение')
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности привычки')

    last_send = models.DateTimeField(verbose_name='Последняя отправка напоминания', **NULLABLE)
