from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse
# Create your views here.

def busqueda_productos(request):
    doc_externo =  open("/home/daniel/Documents/proyectos_980_ejemplos/Proyectos_980_ejemplos/Django/TiendaOnline/gestionpedidos/Template/buqueda_productos.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    mensaje = plt.render(ctx)
    return render(request, mensaje)

def framework (request):
    doc_externo =  open("/home/daniel/Documents/Django/Prueba1/Plantillas/busqueda_productos.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    mensaje = plt.render(ctx)
    return HttpResponse(mensaje)