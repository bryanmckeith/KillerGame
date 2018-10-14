#!/usr/bin/python
# -*- coding: latin-1 -*-

import os.path
from random import randint, shuffle

BASE = os.path.dirname(os.path.abspath(__file__))

def assign_players_a_target(players):
    """ Return killers and their targets as 'Killer':'Target'
        from a list of players """
    killers_and_targets = {}
    targets = list(players)
    shuffle(targets)
    for killer in players:
        if targets.index(killer) < (len(targets)-1):
            killers_and_targets[killer] = targets[targets.index(killer)+1]
        else :
            killers_and_targets[killer] = targets[0]
    return killers_and_targets

def get_actions():
    """ Return actions as a list from file actions.txt """
    with open(os.path.join(BASE, "actions.txt"), "r") as file_actions:
            file_content = file_actions.read()
            actions = file_content.split('\n')
    file_actions.close()
    
    shuffle(actions)

    return actions