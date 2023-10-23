from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = 'Вы не являетесь создателем профиля!'

    def has_object_permission(self, request, view, obj):
        if request.user == obj:
            return True
        return False


class IsStaff(BasePermission):
    message = 'Доступ запрещен!'

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return False