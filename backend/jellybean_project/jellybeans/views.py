from django.http import HttpResponse
from django.shortcuts import render, redirect
# from rest_framework import generics
from .models import Flavor
# from .serializers import FlavorSerializer

# Create your views here.

def indexPageView(request):
    flavors = Flavor.objects.all().values()
    context = {
        'data':flavors,
    }
    return render(request, 'displayFlavor.html', {'data':context})

def createPageView(request):
    return render(request, 'addFlavor.html')

def addFlavorView(request):
    if request.method == 'POST':
        name = request.POST['Flavor']
        color = request.POST['Color']
        description = request.POST['Description']

        flavor = Flavor()

        flavor.Flavor = name
        flavor.Color = color
        flavor.Description = description

        flavor.save()

    return redirect(indexPageView)

def updatePageView(request, sid):
    flavor = Flavor.objects.values().get(id=sid)
    context = {
        'data':flavor
    }
    return render(request, 'updateFlavor.html', {'data':context})

def submitChanges(request,sid):
    flavor = Flavor.objects.get(id=sid)

    if request.method == 'POST':
        name = request.POST['Flavor']
        color = request.POST['Color']
        description = request.POST['Description']

        flavor.Flavor = name
        flavor.Color = color
        flavor.Description = description

        flavor.save()
    return redirect(indexPageView)

def deletePageView(request, sid):
    flavor = Flavor.objects.get(id=sid).delete()
    return redirect(indexPageView)