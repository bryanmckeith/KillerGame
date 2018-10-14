#!/usr/bin/python
# encoding=utf8

from datetime import datetime
from django.db import models
from django.core.validators import RegexValidator

class players(models.Model):

    name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    pseudo = models.CharField(max_length=30, unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,11}$', message="Le format du téléphone n'est pas le bon...")
    telephone = models.CharField(validators=[phone_regex], max_length=11)
    action = models.CharField(max_length=150)
    points = models.IntegerField()
    target = models.CharField(max_length=30)
    code = models.CharField(max_length=8)
    state = models.CharField(max_length=6)
    last_killed_action_date = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "players"
        ordering = ['name']

    def __str__(self):
        return self.name

class murders(models.Model):

    killer = models.CharField(max_length=30)
    target_code = models.CharField(max_length=8)
    action_date = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "murders"
        ordering = ['killer']

    def __str__(self):
        return self.killer

class games(models.Model):

    game = models.CharField(max_length=30)
    status = models.CharField(max_length=1)
    started_date = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "games"
        ordering = ['game']