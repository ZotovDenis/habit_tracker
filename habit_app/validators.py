from rest_framework.serializers import ValidationError


class PleasantHabitValidator:
    """
    Связанная привычка, приятная привычка и вознаграждение.
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        habit_is_pleasant = dict(value).get('is_pleasant')      # приятная привычка
        habit_is_related = dict(value).get('related_habit')     # связанная привычка
        habit_reward = dict(value).get('reward')                # вознаграждение

        if habit_is_pleasant is True and habit_reward is not None:
            raise ValidationError('У приятной привычки не может быть вознаграждения!')

        if habit_is_pleasant is True and habit_is_related is not None:
            raise ValidationError('У приятной привычки не может быть связанной привычки!')

        if habit_is_related and habit_reward is not None:
            raise ValidationError('Нельзя выбрать связанную привычку и вознаграждение одновременно!')


class RelatedHabitValidator:
    """
    Связанной привычкой может быть только приятная привычка.
    """

    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        pleasant_habit = dict(value).get(self.fields)

        if pleasant_habit and not pleasant_habit.is_pleasant:
            raise ValidationError('Связанная привычка должна иметь признак приятной привычки!')


class TimeHabitValidator:
    """
    Время выполнения привычки не должно превышать 120 секунд.
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        time_to_complete = dict(value).get(self.field)
        if time_to_complete >= 120:
            raise ValidationError('Время выполнения привычки не должно превышать 120 секунд!')


class PeriodicityHabitValidator:
    """
    Привычка должна выполняться не реже 1 раза в 7 дней.
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        period_value = dict(value).get(self.field)
        if period_value > 7 or period_value == 0:
            raise ValidationError('Привычка должна выполняться не реже 1 раза в 7 дней!')
