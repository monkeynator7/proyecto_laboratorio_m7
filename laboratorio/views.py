from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from .models import Laboratorio

def inicio_view(request):
    return render(request, 'laboratorio/inicio.html')

def mostrar_laboratorio_view(request): 
    laboratorios = Laboratorio.objects.all()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {'laboratorios': laboratorios, 'num_visits': num_visits}
    return render(request, 'laboratorio/index.html', context)

def insert_view(request):
    return render(request, 'laboratorio/insertar.html')

def insertar_laboratorio_view(request):
    nombre = request.POST['nombre']
    ciudad = request.POST['ciudad']
    pais = request.POST['pais']
    laboratorio = Laboratorio(nombre=nombre, ciudad=ciudad, pais=pais)
    laboratorio.save()
    return HttpResponseRedirect(reverse('mostrar_laboratorio'))

def eliminar_laboratorio_view(request, pk):
    laboratorio = Laboratorio.objects.get(id=pk)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('/laboratorio/mostrar/')
    context = {'laboratorio': laboratorio}
    return render(request, 'laboratorio/eliminar.html', context)

def update_view(request, pk):
    laboratorio = Laboratorio.objects.get(id=pk)
    context = {
        'laboratorio': laboratorio
    }
    return render(request, 'laboratorio/editar.html', context)

def editar_laboratorio_view(request, pk):
    laboratorio = Laboratorio.objects.get(id=pk)
    laboratorio.nombre=request.POST['nombre']
    laboratorio.ciudad=request.POST['ciudad']
    laboratorio.pais=request.POST['pais']
    laboratorio.save()
    return HttpResponseRedirect(reverse('mostrar_laboratorio'))