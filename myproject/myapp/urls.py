#!/usr/bin/python
# encoding=utf8

from django.conf.urls import url
from . import views

urlpatterns = [
    url('home', views.home, name='Home Page'),
    url('subscription', views.subscription, name='Subscription Page'),
    url('ranking', views.ranking, name='Ranking Page'),
    url('rules', views.rules, name='Rules Page'),
    url('error', views.error, name='Error Page'),
    url('welcome', views.welcome, name='Welcome Page'),
    url('welldone', views.welldone, name='Confirm OK Page'),
    url('supportTV', views.supportTV, name='Ranking Page optimized for your TV'),
    url('backD00r', views.backdoor, name='backdoor'),
    url('start_game', views.start_game, name='Game Starter Page'),
]