from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('NuevoCampista', views.nuevocampista, name='NuevoCampista'),
    path('ListadoCampista', views.listadocampista, name='ListadoCampista'),
    path('AgregarCampista', views.agregarcampista, name='AgregarCampista'),
    path('EditarCampista/<int:id>/', views.editarcampista, name='EditarCampista'),
    path('EliminarCampista/<int:id>/', views.eliminarcampista, name='EliminarCampista'),
    path('NuevaReserva/<int:campista_id>/', views.nuevareserva, name='NuevaReserva'),
    path('ListadoReserva',views.listadoreserva,name='ListadoReserva'),
    path('AgregarReserva', views.agregarreserva, name='AgregarReserva'),
    path('EditarReserva/<int:reserva_id>/', views.editarreserva, name='EditarReserva'),
    path('EliminarReserva/<int:id>/', views.eliminarreserva, name='EliminarReserva'),
    
]