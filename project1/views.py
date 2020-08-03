from django.http import HttpResponse
from django.template import Template, Context
import datetime

def helloWorld(request):
    fichero_plantilla=open("project1/templates/helloworld.html") 
    tmpl_helloWorld=Template(fichero_plantilla.read())
    fichero_plantilla.close()
    ctx=Context()
    documento=tmpl_helloWorld.render(ctx)
    return HttpResponse(documento)

def getData(request):
    fechaActual=datetime.datetime.now()
    documento= "<html><body><h3>Fecha y hora actuales %s </h3> </body></html>" % fechaActual
    return HttpResponse(documento) 

def calculaEdad(request,edad,anyo):
    periodo=anyo-2020
    edadFutura=edad+periodo
    documento= "<html><body><h3>En el año %s tendras %s años</h3> </body></html>" %(anyo, edadFutura)
    return HttpResponse(documento)