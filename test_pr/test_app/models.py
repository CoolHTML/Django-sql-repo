# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Clients(models.Model):
    name = models.TextField()

    class Meta:
        db_table = 'clients'


class Durations(models.Model):
    client_id = models.IntegerField()
    equipment_id = models.IntegerField()
    start = models.DateTimeField()
    stop = models.DateTimeField()
    mode_id = models.IntegerField()
    minutes = models.IntegerField()

    class Meta:
        db_table = 'durations'


class Equipment(models.Model):
    client_id = models.IntegerField()
    name = models.TextField()

    class Meta:
        db_table = 'equipment'


class Modes(models.Model):
    name = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        db_table = 'modes'
