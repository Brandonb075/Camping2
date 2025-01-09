from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from .models import *

# Create your views here.

def inicio(request):
    return render(request,'inicio.html')

######################################################################################################
#funciones de campista
#vista de Campista
def nuevocampista(request):
    return render(request,'Campista_crear.html')

#Listado de Campista
def listadocampista(request):
    campista=Campista.objects.all()
    return render (request,'listadocampista.html',{'campista':campista})

#Agregar Campista
def agregarcampista(request):
    #recuperando los datos del formulario
    identificacion=request.POST['txt_identificacion']
    nombre=request.POST['txt_nombre']
    correo=request.POST['txt_correo']
    telefono=request.POST['txt_telefono']
    direccion=request.POST['txt_direccion']
    #crear un objeto dentro de campista
    nuevocampista=Campista.objects.create(
        #guardar los datos recuperados
        identificacion=identificacion,
        nombre=nombre,
        correo=correo,
        telefono=telefono,
        direccion=direccion
    )
    #mover al listado Campista
    return redirect('ListadoCampista')

#Editar Campista
def editarcampista(request, id):
    #objeter informacion
    campista=get_object_or_404(Campista, id=id)
    if request.method=='POST':    
        #guardar nueva informacion
        campista.identificacion=request.POST['txt_identificacion']
        campista.nombre=request.POST['txt_nombre']
        campista.correo=request.POST['txt_correo']
        campista.telefono=request.POST['txt_telefono']
        campista.direccion=request.POST['txt_direccion']
        campista.save()
        #rendireccionar la pagina
        return redirect('ListadoCampista')
    return render (request,'editarcampista.html',{'campista':campista})

#Eliminar Campista
def eliminarcampista(request, id):
    campista = Campista.objects.get(id=id)
    campista.delete()
    return redirect('ListadoCampista')  
    

#####################################################################################################
#funciones de reservas
#vista de Campista
def nuevareserva(request, campista_id):
    campista=get_object_or_404(Campista, id=campista_id)
    return render(request,'Reserva_crear.html',{'campista':campista})

#Listado de Campista
def listadoreserva(request):
    reserva=Reserva.objects.all()
    return render (request,'listadoreserva.html',{'reserva':reserva})

#Agregar Campista
def agregarreserva(request):
    #recuperando los datos del formulario
    campista_id=request.POST['txt_campista']
    campista=get_object_or_404(Campista, id=campista_id)
    fecha_inicio=request.POST['txt_fech_ini']
    fecha_fin=request.POST['txt_fech_fin']
    alojamiento=request.POST['txt_alojamiento']
    numero_personas=request.POST['txt_npersonas']
    Estado=request.POST['txt_estado']
    observaciones=request.POST['txt_observaciones']
    #crear un objeto dentro de campista
    nuevareserva=Reserva.objects.create(
        #guardar los datos recuperados
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin,
        campista=campista,
        alojamiento=alojamiento,
        numero_personas=numero_personas,
        Estado=Estado,
        observaciones=observaciones
    )
    #mover al listado Campista
    return redirect('ListadoReserva')

#Editar Campista
def editarreserva(request, reserva_id):
    #objeter informacion
    reserva=get_object_or_404(Reserva, id=reserva_id)
    if request.method=='POST':    
        campista_id=request.POST['txt_campista']
        campista=get_object_or_404(Campista, id=campista_id)
        #guardar nueva informacion
        reserva.fecha_inicio=request.POST['txt_fech_ini']
        reserva.fecha_fin=request.POST['txt_fech_fin']
        reserva.campista=campista
        reserva.alojamiento=request.POST['txt_alojamiento']
        reserva.numero_personas=request.POST['txt_npersonas']
        reserva.Estado=request.POST['txt_estado']
        reserva.observaciones=request.POST['txt_observaciones']
        reserva.save()
        #rendireccionar la pagina
        return redirect('ListadoReserva')
    return render (request,'editarreserva.html',{'reserva':reserva, 'campista':reserva.campista})

#Eliminar Campista
def eliminarreserva(request, id):
    reserva = Reserva.objects.get(id=id)
    reserva.delete()
    return redirect('ListadoReserva')  
    