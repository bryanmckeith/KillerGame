#!/usr/bin/python
# encoding=utf8

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from datetime import datetime

from ..forms import start_game_form
from ..models import players, murders, games

from getcode import get_code
from link import assign_players_a_target, get_actions
from messaging import send_SMS

# ----- Pages Administration ----- #
def start_game(request):

    form = start_game_form(request.POST or None)
    
    if form.is_valid():

        game = games.objects.get(game="my_game")

        if game.status == "0":

            game.status = "1"
            game.started = datetime.now()
            game.save()

            players_pseudos_list = list()

            for player in players.objects.all():
                players_pseudos_list.append(player.pseudo)

            killers_and_targets = assign_players_a_target(players_pseudos_list)
            actions = get_actions()
            i = 0

            for link in killers_and_targets.items() :

                killer = players.objects.get(pseudo = link[0])
                killer.target = link[1]
                killer.save()
                
                target = players.objects.get(pseudo = link[1])
                target.action = actions[i]
                target.save()
                
                i += 1
                """ In case len(actions) < len(myUsers) : """
                i %= len(actions)
                
            first_names_list = list()
            telephones_list = list()
            targets_list = list()
            actions_list = list()
            
            for player in players.objects.all():

                first_names_list.append(player.first_name)
                telephones_list.append(player.telephone)
                killer_target = players.objects.get(pseudo = player.target)
                targets_list.append(killer_target.first_name \
                                + " " \
                                + killer_target.name)
                actions_list.append(killer_target.action)
                
            i = 0
            for player_first_name in first_names_list :
                message = "La chasse est ouverte " \
                          + player_first_name \
                          + "! Voici votre 1ère cible : " \
                          + targets_list[i] \
                          + ". Votre mission, si vous l'acceptez : " \
                          + actions_list[i] \
                          + ". Bonne chasse !"
                send_SMS(telephones_list[i], message)
                i += 1
            
            players_list = players.objects.all()
            return render(request, 'myapp/backdoor.html', {'players_list':players_list})
        
        else: 
            game.status = "0"
            game.save()
            players_list = players.objects.all()
            return render(request, 'myapp/backdoor.html', {'players_list':players_list})
        
    return render(request, 'myapp/start_game.html', locals())

def backdoor(request):
    players_list = players.objects.all()
    return render(request, 'myapp/backdoor.html', {'players_list':players_list})
