from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):

    username = models.CharField(max_length=100, unique=True, verbose_name="Имя пользователя в ТГ")
    chat_id = models.PositiveBigIntegerField(default=0, unique=True, verbose_name="ID чата", **NULLABLE)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
