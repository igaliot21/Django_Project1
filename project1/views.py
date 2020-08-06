from django.http import HttpResponse
from django.template import Template, Context, loader
import datetime

class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

def helloWorld(request):
    fichero_plantilla=open("project1/templates/helloworld.html") 
    tmpl_helloWorld=Template(fichero_plantilla.read())
    fichero_plantilla.close()
    ctx=Context()
    documento=tmpl_helloWorld.render(ctx)
    return HttpResponse(documento)

def helloWorldVar(request):    
    p=Persona("Jose Mª","Izquierdo")
    caracteristica="gilipollas"
    ahora=datetime.datetime.now()
    fichero_plantilla=open("project1/templates/helloworldvar.html") 
    tmpl_helloWorld=Template(fichero_plantilla.read())
    fichero_plantilla.close()
    ctx=Context({"persona":p,"caracteristica":caracteristica, "ahora":ahora})
    documento=tmpl_helloWorld.render(ctx)
    return HttpResponse(documento)

def helloWorldVar2(request):
    p=Persona("Jose Mª","Izquierdo") 
    caracteristica="gilipollas"
    ahora=datetime.datetime.now()
    temas=["plantillas","modelos","formularios","vistas","despliegue de aplicación"]
    temasVacio=[]
    fichero_plantilla=open("project1/templates/helloworldvar2.html") 
    tmpl_helloWorld=Template(fichero_plantilla.read())
    fichero_plantilla.close()
    ctx=Context({"persona":p,"caracteristica":caracteristica, "ahora":ahora, "temas":temas})
    documento=tmpl_helloWorld.render(ctx)
    return HttpResponse(documento)    

def helloWorldVar3(request):
    p=Persona("Jose Mª","Izquierdo") 
    caracteristica="gilipollas"
    ahora=datetime.datetime.now()
    temas=["plantillas","modelos","formularios","vistas","despliegue de aplicación"]
    temasVacio=[]
    
    #fichero_plantilla=open("project1/templates/helloworldvar3.html") 
    #tmpl_helloWorld=Template(fichero_plantilla.read())
    #fichero_plantilla.close()
    fichero_plantilla=loader.get_template("helloworldvar3.html")
     
    #ctx=Context({"persona":p,"caracteristica":caracteristica, "ahora":ahora, "temas":temas})
    documento=fichero_plantilla.render({"persona":p,"caracteristica":caracteristica, "ahora":ahora, "temas":temas})
    
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