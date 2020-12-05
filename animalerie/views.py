from django.shortcuts import render, get_object_or_404
from .models import Animal, Equipement


def animalerie(request):
    animaux = Animal.objects.all()
    equipements = Equipement.objects.all()
    message_type, message = "", ""

    if request.method == "GET":
        if 'animal' and 'equipement' in request.GET:
            id_equip = request.GET['equipement']
            animal = Animal.objects.get(id_animal=request.GET['animal'])
            if id_equip == "litière":
                message_type, message = animal.reveiller()
            elif id_equip == "mangeoire":
                message_type, message = animal.nourrir()
            elif id_equip == "roue":
                message_type, message = animal.divertir()
            elif id_equip == "nid":
                message_type, message = animal.coucher()

    return render(request, 'animalerie/animalerie.html', {
        'animaux': animaux,
        'equipements': equipements,
        'type': message_type,
        'message': message
    })


def animal_detail(request, id_animal):
    animal = get_object_or_404(Animal, id_animal=id_animal)
    message_type, message = "", ""

    if request.method == "GET":
        if 'action' in request.GET:
            action = request.GET["action"]
            if action == "reveiller":
                message_type, message = animal.reveiller()
            elif action == "nourrir":
                message_type, message = animal.nourrir()
            elif action == "divertir":
                message_type, message = animal.divertir()
            elif action == "coucher":
                message_type, message = animal.coucher()

    return render(request, 'animalerie/animal_detail.html', {
        'animal': animal,
        'type': message_type,
        'message': message
    })

def equipement_detail(request, id_equip):
    equipement = get_object_or_404(Equipement, id_equip=id_equip)
    return render(request, 'animalerie/equipement_detail.html', {'equipement': equipement})

