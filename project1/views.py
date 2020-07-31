from django.http import HttpResponse
import datetime

def helloWorld(request):
    return HttpResponse("Hello world")

def getData(request):
    fechaActual=datetime.datetime.now()
    #documento= "<html><body><h3>Fecha y hora actuales " + fechaActual + "</h3> </body></html>"
    documento= "<html><body><h3>Fecha y hora actuales %s </h3> </body></html>" % fechaActual
    return HttpResponse(documento) 

def calculaEdad(request,edad,anyo):
    periodo=anyo-2020
    edadFutura=edad+periodo
    documento= "<html><body><h3>En el año %s tendras %s años</h3> </body></html>" %(anyo, edadFutura)
    return HttpResponse(documento)