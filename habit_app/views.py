from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from habit_app.models import Habit
from habit_app.pagination import PagePagination
from habit_app.permissons import IsOwner, IsStaff
from habit_app.serializers import HabitSerializers


class HabitCreateAPIView(generics.CreateAPIView):
    """ Создание Привычки """
    serializer_class = HabitSerializers
    permission_classes = [IsAuthenticated]


class HabitListAPIView(generics.ListAPIView):
    """ Контроллер вывода всех Привычек"""
    serializer_class = HabitSerializers
    pagination_class = PagePagination
    permission_classes = [IsAuthenticated, IsStaff | IsOwner]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitPublicListAPIView(generics.ListAPIView):
    """ Просмотр всех публичных Привычек """
    serializer_class = HabitSerializers
    pagination_class = PagePagination
    permission_classes = [AllowAny]
    queryset = Habit.objects.filter(is_public=True).order_by('-id')


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """ Контроллер просмотра привычки по ID """
    serializer_class = HabitSerializers
    permission_classes = [IsAuthenticated & IsOwner]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitUpdateAPIView(generics.UpdateAPIView):
    """ Контроллер изменения Привычки """
    serializer_class = HabitSerializers
    permission_classes = [IsAuthenticated & IsOwner]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Контроллер удаления Привычки"""

    permission_classes = [IsAuthenticated & IsOwner]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)
