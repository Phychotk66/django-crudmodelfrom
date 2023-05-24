from django.shortcuts import render, HttpResponseRedirect
from .forms import Registion
from .models import Vser
# Create your views here.
def User (request):
     if request.method == 'POST':
       fm = Registion(request.POST)
       if fm.is_valid():
         nm = fm.cleaned_data['name']
         em = fm.cleaned_data['email']
         ps = fm.cleaned_data['password']
         ms = fm.cleaned_data['massages']
         reg = Vser(name=nm, email=em, password=ps, massages=ms)
         reg.save()
         fm = Registion()
     else:
        fm = Registion()
     Student = Vser.objects.all()
     return render(request, 'base.html', {'from':fm, 'Std':Student})

def delete(request, id):
   if request.method == 'POST':
     pi = Vser.objects.get(pk=id)
     pi.delete()
   return HttpResponseRedirect('/')



def update(request, id):
  if request.method == 'POST':
    pi = Vser.objects.get(pk=id)
    fm = Registion(request.POST, instance=pi)
    if fm.is_valid():
      fm.save()
    
  else:
     pi = Vser.objects.get(pk=id)
     fm = Registion(instance=pi)

  return render(request, 'from.html' , {'from':fm})

