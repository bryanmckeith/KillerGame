#!/usr/bin/python
# encoding=utf8

from django import forms
from .models import players, murders, games

class subscription_form(forms.ModelForm):
    
    name = forms.CharField(label='')
    first_name = forms.CharField(label='')
    pseudo = forms.CharField(label='')
    telephone = forms.CharField(label='')
    
    class Meta:
        model = players
        fields = ('name', 'first_name', 'pseudo', 'telephone',)

    def __init__(self, *args, **kwargs):
        super(subscription_form, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'NOM'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Prénom'
        self.fields['pseudo'].widget.attrs['placeholder'] = 'Choisissez un pseudo'
        self.fields['telephone'].widget.attrs['placeholder'] = 'Téléphone'

class murder_form(forms.ModelForm):
    
    killer = forms.CharField(label='')
    target_code = forms.CharField(label='')
    
    class Meta:
        model = murders
        exclude = ('action_date',)

    def __init__(self, *args, **kwargs):
        super(murder_form, self).__init__(*args, **kwargs)
        self.fields['killer'].widget.attrs['placeholder'] = 'Votre pseudo'
        self.fields['target_code'].widget.attrs['placeholder'] = 'Code de validation'

class start_game_form(forms.ModelForm):

    class Meta:
        model = games
        exclude = ('game', 'status', 'started_date',)

    def __init__(self, *args, **kwargs):
        super(start_game_form, self).__init__(*args, **kwargs)