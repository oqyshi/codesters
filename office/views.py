from django.shortcuts import render
from django.views.generic.base import View
# from annoying.functions import get_object_or_None
# from celery import shared_task
import requests
from random import choice
from .quotes import QUOTES
import random
import json
from django.http import JsonResponse


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class GameView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'office/game.html')


def get_quote(request):
    return JsonResponse({"quote": choice(QUOTES)})


def get_health(request, uid: int):
    data = []
    for _ in range(10):
        data.append({'y': random.randrange(1, 5)})
    return JsonResponse({"health_data": data})


def get_random_recipe(request):
    recipe = random.choice(json.loads(open("static/json/Recipes.json", "r").read()))
    return {
        "name": recipe["name"],
        "health_score": recipe["health_score"]
    }
