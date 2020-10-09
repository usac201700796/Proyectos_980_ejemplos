from django.http import HttpResponse
import datetime
from django.template import Template, Context

def response1 (request): 
    return HttpResponse("Proyectos de Computacion Orientados a Ingenieria Electronica")

def response2 (request):
    return HttpResponse("Adios")

# Mostramos Fecha Actual

def fecha (request):
    fecha_actual = datetime.datetime.now()
    mensaje = """<html>
    <body>
    <h1>
    Proyectos de Computacion Orientados a Ingenieria Electronica %s
    </h1>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(mensaje)


# Caculamos cuantos años tendremos en N años
def calcular_edad (request, year):
    edad_actual = 18
    periodo = year - 2020
    edad_futura = edad_actual+periodo
    mensaje = "<html><body><h2>En el año %s tendras %s años" % (year,edad_futura)

    return HttpResponse(mensaje)

def framework (request):
    doc_externo =  open("/home/daniel/Documents/Django/Prueba1/Plantillas/plantilla.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    mensaje = plt.render(ctx)
    return HttpResponse(mensaje)