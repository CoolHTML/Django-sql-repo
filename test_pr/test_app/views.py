from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
# Create your views here.
from .forms import *
def main_page(request):
    title = 'Главная страница'
    equipment= Equipment.objects.all()
    clients = Clients.objects.all()
    data={}
    timer = 0
    if request.method == 'POST':
        form = mainform(request.POST)
        print(form.is_valid())
        if form.is_valid():
            a = form.cleaned_data
            print(a)
            print(int(a['client']))
            if(int(a['client']) > 0):
                timer+=1
                sq1 = f'client_id = {a["client"]}'
            else:
                sq1=''
            print(int(a["equipment"]))
            if(int(a["equipment"]) > 0):
                if(timer):
                    sq1+=' AND '
                timer+=1
                sq2 = f'equipment_id = {a["equipment"]}'
            else:
                sq2 = ''
            print(int(a["modes"]))
            if(int(a["modes"]) != -7):
                if(timer):
                    sq2+=' AND '
                timer+=1
                sq3 = f'mode_id = {a["modes"]}'
            else:
                sq3 = ''
            if(int(a["durations"])>-1):
                if(timer):
                    sq3+=' AND '
                timer+=1
                sq4 = f'minutes >= {a["durations"]}'
            if(a["start_date"] != 1):
                print(123)



            print(f'SELECT * FROM Durations WHERE  {sq1} {sq2}')
            data = Durations.objects.raw(f'SELECT * FROM Durations WHERE {sq1}{sq2}{sq3}{sq4}')
            print(data)
            #return HttpResponseRedirect(request.path)
    else:
        form = mainform()
    return render(request,'test_app/main_page.html',{'title':title,'equipment':equipment, 'clients':clients,'mainform':mainform,'data':data})