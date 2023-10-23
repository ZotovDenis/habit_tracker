from rest_framework.permissions import BasePermission


class IsStaff(BasePermission):
    message = 'Вы не являетесь администратором!'

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return False


class IsOwner(BasePermission):
    message = 'Вы не являетесь создателем привычки!'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False
