from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.list_services, name='list_services'),
    path('adicionar/', views.add_services, name='add_services'),
    path('editar/<int:id_services>/', views.edit_services, name='edit_services'),
    path('excluir/<int:id_services>/', views.delete_services, name='delete_services'),
]