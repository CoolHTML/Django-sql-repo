from django import forms
from .models import *


equipment = Equipment.objects.all()
clients = Clients.objects.all()
modes = Modes.objects.all()
durations = Durations.objects.all()


equipment_=[(0,'-'),(0,'Все')]
for i in equipment:
    equipment_.append((i.pk,i.name))
equipment_=tuple(equipment_)


clients_=[(0,'-'),(0,'Все')]
for i in clients:
    clients_.append((i.pk,i.name))
clients_=tuple(clients_)

modes_=[(-7,'-'),(-7,'Все')]
for i in modes:
    modes_.append((i.pk,i.name))
modes_=tuple(modes_)

time=[(-1,'-')]
for i in range(0,24):
    time.append((i,i))
time = tuple(time)

class mainform(forms.Form):
    client = forms.ChoiceField(
    choices=clients_
    )
    equipment = forms.ChoiceField(
    choices=equipment_
    )
    modes = forms.ChoiceField(
    choices=modes_
    )
    durations = forms.IntegerField()
    start_date = forms.DateField()
    end_date = forms.DateField()

    start_time = forms.ChoiceField(
        choices = time
    )
    endtime = forms.ChoiceField(
        choices = time
    )















