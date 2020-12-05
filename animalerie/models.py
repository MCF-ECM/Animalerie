from django.db import models


class Equipement(models.Model):
    id_equip = models.CharField(max_length=100, primary_key=True)
    disponibilite = models.CharField(max_length=20)
    photo = models.CharField(max_length=200)

    def __str__(self):
        return self.id_equip

    def occupants(self):
        occupants = []
        for animal in Animal.objects.all():
            if animal.lieu.id_equip == self.id_equip:
                occupants.append(animal)
        return occupants


class Animal(models.Model):
    id_animal = models.CharField(max_length=100, primary_key=True)
    etat = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    race = models.CharField(max_length=20)
    photo = models.CharField(max_length=200)
    lieu = models.ForeignKey(Equipement, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_animal

    def nourrir(self):
        if self.etat == "affamé":
            mangeoire = Equipement.objects.get(id_equip='mangeoire')
            if mangeoire.disponibilite == "libre":
                self.lieu.disponibilite = "libre"
                self.lieu.save()

                self.lieu = mangeoire
                self.etat = "repus"
                self.save()

                mangeoire.disponibilite = "occupé"
                mangeoire.save()

                return "info", "Félicitation, " + self.id_animal + " a rejoint la mangeoire et est maintenant repus."
            else:
                return "danger", "Impossible, la mangeoire est actuellement occupée par " + mangeoire.occupants()[0].id_animal + ". "
        else:
            return "danger", "Désolé, " + self.id_animal + " n'a pas faim!"

    def divertir(self):
        if self.etat == "repus":
            roue = Equipement.objects.get(id_equip='roue')
            if roue.disponibilite == "libre":
                self.lieu.disponibilite = "libre"
                self.lieu.save()

                self.lieu = roue
                self.etat = "fatigué"
                self.save()

                roue.disponibilite = "occupé"
                roue.save()

                return "info", "Félicitation, " + self.id_animal + " a rejoint la roue et est maintenant fatigué."
            else:
                return "danger", "Impossible, la roue est actuellement occupée par " + roue.occupants()[0].id_animal + "."
        else:
            return "danger", "Désolé, " + self.id_animal + " n'est pas en état de faire du sport!"

    def coucher(self):
        if self.etat == "fatigué":
            nid = Equipement.objects.get(id_equip='nid')
            if nid.disponibilite == "libre":
                self.lieu.disponibilite = "libre"
                self.lieu.save()

                self.lieu = nid
                self.etat = "endormi"
                self.save()

                nid.disponibilite = "occupé"
                nid.save()

                return "info", "Félicitation, " + self.id_animal + " a rejoint le nid et est maintenant endormi."
            else:
                return "danger", "Impossible, la nid est actuellement occupée par " + nid.occupants()[0].id_animal + "."
        else:
            return "danger", "Désolé, " + self.id_animal + " n'est pas fatigué!"

    def reveiller(self):
        if self.etat == "endormi":
            self.lieu.disponibilite = "libre"
            self.lieu.save()

            self.lieu = Equipement.objects.get(id_equip='litière')
            self.etat = "affamé"
            self.save()

            return "info", "Félicitation, " + self.id_animal + " a rejoint la litière et est maintenant affamé."
        else:
            return "danger", "Désolé, " + self.id_animal + " ne dort pas!"
