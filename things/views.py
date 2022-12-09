from django.shortcuts import render
from .forms import ThingForm

def Thingsform(request):
    form = ThingForm()
    return render(request, 'home.html', {'form': form})
