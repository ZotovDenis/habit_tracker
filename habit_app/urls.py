from django.urls import path

from habit_app.apps import HabitAppConfig
from habit_app.views import HabitCreateAPIView, HabitListAPIView, HabitPublicListAPIView, HabitRetrieveAPIView, \
    HabitUpdateAPIView, HabitDestroyAPIView

app_name = HabitAppConfig.name

urlpatterns = [
    path('habit/create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('habit/', HabitListAPIView.as_view(), name='habit_list'),
    path('public_habit/', HabitPublicListAPIView.as_view(), name='public_habit_list'),
    path('habit/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit_detail'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_delete'),
]
