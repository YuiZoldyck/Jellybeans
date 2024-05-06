from django.shortcuts import render, redirect
from .models import Flavor

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
        rating = float(request.POST['Rating'])
        
        flavor = Flavor()

        flavor.Flavor = name
        flavor.Color = color
        flavor.Description = description
        flavor.Rating = rating

        try:
            if rating < 0 or rating > 5:
                raise ValueError
        except ValueError:
            error_message = "Invalid rating value. Rating must be between 0 and 5."
            return render(request, 'addflavor.html', {'error': error_message, 'flavor_data': flavor})
        

        flavor.save()

    return redirect(indexPageView)

def updatePageView(request, sid):
    flavor = Flavor.objects.values().get(id=sid)
    context = {
        'flavor':flavor
    }
    return render(request, 'updateFlavor.html', context)

def submitChanges(request,sid):
    flavor = Flavor.objects.get(id=sid)

    if request.method == 'POST':
        name = request.POST['Flavor']
        color = request.POST['Color']
        description = request.POST['Description']
        rating = float(request.POST['Rating'])

        flavor.Flavor = name
        flavor.Color = color
        flavor.Description = description
        flavor.Rating = rating

        try:
            if rating < 0 or rating > 5:
                raise ValueError
        except ValueError:
            error_message = "Invalid rating value. Rating must be between 0 and 5."
            return render(request, 'updateFlavor.html', {'error': error_message, 'flavor': flavor})

        flavor.save()
    return redirect(indexPageView)

def deletePageView(request, sid):
    flavor = Flavor.objects.get(id=sid).delete()
    return redirect(indexPageView)