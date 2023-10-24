from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.permissons import IsStaff, IsOwner
from users.models import User
from users.serializers import UserSerializer, UserCreateSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """ Контроллер создания Пользователя """
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]


class UserListAPIView(generics.ListAPIView):
    """ Контроллер вывода списка Пользователей """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated & IsStaff]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """ Контроллер просмотра Пользователя """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated & IsOwner]


class UserUpdateAPIView(generics.UpdateAPIView):
    """ Контроллер изменения Пользователя """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated & IsOwner]


class UserDestroyAPIView(generics.DestroyAPIView):
    """ Контроллер удаления Пользователя """
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated & IsOwner]
