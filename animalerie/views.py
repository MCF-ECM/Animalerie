from django.shortcuts import render, get_object_or_404
from .models import Animal, Equipement


def animalerie(request):
    animaux = Animal.objects.all()
    equipements = Equipement.objects.all()

    return render(request, 'animalerie/animalerie.html', {
        'animaux': animaux,
        'equipements': equipements,
    })


def animal_detail(request, id_animal):
    animal = get_object_or_404(Animal, id_animal=id_animal)
    return render(request, 'animalerie/animal_detail.html', {'animal': animal})

def equipement_detail(request, id_equip):
    equipement = get_object_or_404(Equipement, id_equip=id_equip)
    return render(request, 'animalerie/equipement_detail.html', {'equipement': equipement})

