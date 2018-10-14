#!/usr/bin/python
# encoding=utf8

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from ..forms import subscription_form
from ..models import games

from getcode import get_code
from messaging import send_SMS


# ----- Page Inscription ----- #
def subscription(request):
    
    form = subscription_form(request.POST or None)

    if form.is_valid():
        
        current_game = games.objects.get(game = "my_game")

        if current_game.status == "1":
            """ Status = 1 for games that have already started """
            
            message = "Les inscriptions sont closes, la partie a déjà démarré :("

            return render(request, 'myapp/error.html', {'message': message})

        else :

            new_player = form.save(commit = False)
            recipient = new_player.telephone
            new_player.code = get_code(new_player.name,
                                 new_player.first_name,
                                 new_player.pseudo,
                                 new_player.telephone)
            
            message = "Bienvenue " \
                      + new_player.first_name \
                      + " ! Votre inscription au Killer Game est validée. Votre pseudo = " \
                      + new_player.pseudo \
                      + ". Le code (secret) à donner à votre assassin s'il vous élimine = " \
                      + new_player.code \
                      + ". Vous recevrez votre 1ère mission par SMS lorsque la partie aura démarré. Bonne chasse ! Lien vers le jeu : http://goo.gl/RDYK85"

            SMS_status = send_SMS(recipient, message)

            if SMS_status == 200 :
                
                new_player.action = "_defaultAction"
                new_player.points = 10 # 10 points are given to all new players
                new_player.target = "_defaulttoKill"
                new_player.state = "alive"
                new_player.save()

                return render(request, 'myapp/welcome.html',
                              {'prenom':new_player.first_name} )

            else :

                message = "Nous n'avons pas réussi à vous envoyer un SMS, pouvez-vous vérifier votre numéro de téléphone ?"

                return render(request, 'myapp/error.html', {'message': message})

    return render(request, 'myapp/subscription.html', locals())

