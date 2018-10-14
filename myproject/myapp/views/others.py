#!/usr/bin/python
# encoding=utf8

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from ..models import players

# ----- Killers Ranking Page ----- #
def ranking(request):
    
    ranked_players = players.objects.order_by('-points',
                                       'state',
                                       'last_killed_action_date')

    return render(request, 'myapp/ranking.html',
                  {'ranked_players':ranked_players} )

# ----- Killers Ranking Page optimized for your TV ----- #
def supportTV(request):

    top3 = players.objects.order_by('-points',
                                    'state',
                                    '-last_killed_action_date')[:3]
    top10 = players.objects.order_by('-points',
                                     'state',
                                     '-last_killed_action_date')[3:10]
    top20 = players.objects.order_by('-points',
                                     'state',
                                     '-last_killed_action_date')[10:20]
    top50 = players.objects.order_by('-points',
                                     'state',
                                     '-last_killed_action_date')[20:50]

    return render(request, 'myapp/supportTV.html',
                  {'top3' : top3, 'top10' : top10,
                   'top20' : top20, 'top50' : top50} )

# ----- Killer Game Rules ----- #
def rules(request):

    return render(request, 'myapp/rules.html', locals())

# ----- Error Page ----- #
def error(request):

    return render(request, 'myapp/error.html', locals())

# ----- Subscription Welcome Page ----- #
def welcome(request):

    return render(request, 'myapp/welcome.html', locals())

# ----- Murder Confirmation Page ----- #
def welldone(request):

    return render(request, 'myapp/welldone.html', locals())
