from celery import shared_task
import datetime

from config.settings import TELEGRAM_API_TOKEN, TELEGRAM_URL_BOT
import requests

from habit_app.models import Habit


@shared_task
def send_habit():
    """ Отправка уведомления в Telegram-бота """

    now = datetime.datetime.now()
    now_hour = datetime.datetime.now().hour
    now_minute = datetime.datetime.now().minute
    telegram_bot_token = TELEGRAM_API_TOKEN
    telegram_bot_url = TELEGRAM_URL_BOT

    for habit in Habit.objects.filter(time__hour=now_hour, time__minute=now_minute):

        user_chat_id = habit.user.chat_id

        if habit.reward:
            reward = habit.reward
        elif habit.related_habit:
            reward = habit.related_habit.action
        else:
            reward = 'Ты молодец!'

        text = (f'Напоминание о выполнении привычки!'
                f'\n\nНеобходимо выполнить: {habit.action}'
                f'\nВремя: {habit.time}'
                f'\nМесто: {habit.place}'
                f'\nВремя на выполнение: {habit.time_to_complete} секунд'
                f'\nВознаграждение: {reward}'
                )

        if habit.last_send:
            last_send_date = habit.last_send.date()

            if last_send_date <= now.date() - datetime.timedelta(days=habit.periodicity):

                url = f'{telegram_bot_url}{telegram_bot_token}/sendMessage?chat_id={user_chat_id}&text={text}'
                requests.get(url)
                habit.last_send = now
                habit.save()

        else:
            url = f'{telegram_bot_url}{telegram_bot_token}/sendMessage?chat_id={user_chat_id}&text={text}'
            requests.get(url)
            habit.last_send = now
            habit.save()
