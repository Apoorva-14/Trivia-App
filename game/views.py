from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'game/home.html')

def cricketer(request):
    return render(request, 'game/cricketer.html')


def flag(request):
    return render(request, 'game/flag.html')


def summary(request):
    name = request.GET.get('name')
    cricketer = request.GET.get('cricketer')
    flag = request.GET.get('flag')
    return render(request, 'game/summary.html', {'name':name,'cricketer':cricketer,'flag':flag})


def history(request):
    return render(request, 'game/history.html')
