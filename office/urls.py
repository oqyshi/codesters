from django.urls import path

from . import views

app_name = 'office'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('gameroom/', views.GameView.as_view(), name='game'),
    path('quote/', views.get_quote, name='quote'),
    path('health/<int:uid>', views.get_health, name='health'),

]
