from django.shortcuts import render
from .models import Animal, Equipement


def animalerie(request):
    animaux = Animal.objects.all()
    equipements = Equipement.objects.all()

    return render(request, 'animalerie/animalerie.html', {
        'animaux': animaux,
        'equipements': equipements,
    })
