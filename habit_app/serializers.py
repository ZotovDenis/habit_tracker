from rest_framework import serializers

from habit_app.models import Habit
from habit_app.validators import PleasantHabitValidator, RelatedHabitValidator, TimeHabitValidator, \
    PeriodicityHabitValidator


class HabitSerializers(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = (
            'id', 'user', 'place', 'time', 'action', 'is_pleasant', 'related_habit', 'periodicity', 'reward',
            'time_to_complete', 'is_public'
        )

        validators = [PleasantHabitValidator(fields),
                      RelatedHabitValidator(fields),
                      TimeHabitValidator(field='time_to_complete'),
                      PeriodicityHabitValidator(field='periodicity')]


class HabitDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

    def delete(self):
        instance = self.instance
        instance.delete()