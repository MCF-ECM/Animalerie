from django.urls import path
from . import views


urlpatterns = [
    path('', views.animalerie, name='animalerie'),
    path('animal/<str:id_animal>', views.animal_detail, name='animal_detail'),
    path('equipement/<str:id_equip>', views.equipement_detail, name='equipement_detail'),
]
