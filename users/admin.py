from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_superuser', 'is_staff', 'username', 'chat_id', 'is_active')
    search_fields = ('username', 'chat_id')
    list_filter = ('is_superuser', 'is_staff', 'is_active')