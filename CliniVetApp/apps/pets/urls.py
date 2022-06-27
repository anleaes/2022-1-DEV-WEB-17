from django.urls import path
from . import views

app_name = 'pets'

urlpatterns = [
    path('', views.list_pets, name='list_pets'),
    path('adicionar/', views.add_pets, name='add_pets'),
    path('editar/<int:id_pets>/', views.edit_pets, name='edit_pets'),
    path('excluir/<int:id_pets>/', views.delete_pets, name='delete_pets'),
]
