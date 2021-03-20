from django.shortcuts import render
from django.views.generic.base import View
# from annoying.functions import get_object_or_None
# from celery import shared_task
import requests


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class GameView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'office/game.html')

# @shared_task(ignore_result=True)
# def create_message_notifications(message_id):
#     message = get_object_or_None(Message, id=message_id)
#     if not message:
#         return
#
#     notification = Notification.objects.create(
#         ...
#     )
#     requests.get('http://localhost:3000/new/{}'.format(user_id))
