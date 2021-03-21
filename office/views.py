from django.shortcuts import render, redirect, reverse
from django.views.generic.base import View
from random import choice
from .quotes import QUOTES
import random
import json
from django.http import JsonResponse
from django import template


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class WhiteboardView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'office/whiteboard.html')


class GameView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'office/game.html')


class HealtView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'office/health.html')


class RecipyView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'office/recipy.html')


def get_quote(request):
    return JsonResponse({"quote": choice(QUOTES)})


def get_health(request, uid: int):
    data = []
    for _ in range(10):
        data.append({'y': random.randrange(1, 5)})
    return JsonResponse({"health_data": data})


def get_random_recipe(request):
    recipe = random.choice(json.loads(open("static/json/Recipes.json", "r").read()))
    return JsonResponse({
        "name": recipe["name"],
        "health_score": recipe["health_score"]
    })
