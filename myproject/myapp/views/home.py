#!/usr/bin/python
# encoding=utf8

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from datetime import datetime

from ..forms import murder_form
from ..models import players, games

from messaging import send_SMS

# ----- Home Page ----- #
def home(request):
    
    form = murder_form(request.POST or None)

    if form.is_valid():

        murder = form.save(commit = False)
        
        try:
            killer = players.objects.get(pseudo = murder.killer)
        except players.DoesNotExist:
            message = "Votre pseudo n'est pas reconnu, veuillez recommencer..."
            return render(request, 'myapp/error.html', {'message': message})

        try:
            killer_target = players.objects.get(pseudo = killer.target)
        except players.DoesNotExist:
            message = "Un peu de patience, attendez que la partie soit lancée !"
            return render(request, 'myapp/error.html', {'message': message})

        if (murder.target_code == killer_target.code):
            if (killer_target.state == "alive") :

                murder.save()
                
                killer.points = killer.points + killer_target.points
                killer.target = killer_target.target
                killer.last_killed_action_date = datetime.now()
                killer.save()
                
                killer_target.state = "killed"
                killer_target.target = "_none"
                killer_target.save()
                
                if (killer.target == killer.pseudo) :
                    """ This only happens if you're the last survivor """
                    recipient = killer.telephone
                    message = "Bravo " \
                              + killer.first_name \
                              + " ! Vous êtes le/la dernier-e survivant-e \
du jeu ! Vous avez gagné !!"
                else:
                    new_killer_target = players.objects.get(pseudo = killer.target)
                    recipient = killer.telephone
                    message = "Bravo " \
                              + killer.first_name \
                              + " ! Votre prochaine cible : " \
                              + new_killer_target.first_name \
                              + " " \
                              + new_killer_target.name \
                              + ". Votre mission, si vous l'acceptez : " \
                              + new_killer_target.action \
                              + ". Bonne chasse !"
                SMSstatus = send_SMS(recipient, message)
                if SMSstatus == 200 :
                    return render(request, 'myapp/welldone.html',
                                  {'points': target.points} )
                else :
                    message = "Nous n'avons pas réussi à vous envoyer \
votre nouveau contrat, merci de vous rapprocher du maître du jeu"
                    return render(request, 'myapp/error.html',
                                  {'message': message} )
            else:
                message = "Bien joué 007, \
mais il n'est pas possible de tuer 2 fois la même personne..."
                return render(request, 'myapp/error.html', {'message': message})
        else:
            if (murder.target_code == killer.code):
                message = "C'est pas votre code qu'il faut renseigner, \
c'est celui de votre VICTIME..."
                return render(request, 'myapp/error.html', {'message': message})
            else:
                message = "Le code de validation de votre contrat \
n'est pas bon, veuillez recommencer."
                return render(request, 'myapp/error.html', {'message': message})

    games_list = games.objects.all()
    return render(request, 'myapp/home.html',
                  {'form': form, 'games_list': games_list} )
