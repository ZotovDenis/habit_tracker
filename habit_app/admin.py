from django.contrib import admin

from habit_app.models import Habit


@admin.register(Habit)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'time', 'action', 'is_pleasant', 'related_habit', 'periodicity', 'reward', 'time_to_complete',
        'is_public'
    )
    search_fields = ('user', 'action', 'reward')
    list_filter = ('user',)
