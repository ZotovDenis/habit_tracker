from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """ Проверка на создателя привычки """

    message = 'Вы не являетесь создателем привычки!'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False
