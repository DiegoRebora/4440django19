from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

def saludo(request):
    saludo = "SALUDO"
    pagina_html = HttpResponse(saludo)
    return pagina_html

def saludar_con_fecha(request):
    hoy = datetime.now()
    saludo = f"QUE VERGA ESTO, {hoy.day}/{hoy.month}"
    pagina_html = HttpResponse(saludo)
    return pagina_html

def saludo_con_nombre(request, nombre):
    saludo = f"Hola {nombre}"
    pagina_html = HttpResponse(saludo)
    return pagina_html

"""""  NO ANDA!!!
def saludoreturn(request):
    return "<br><br>a ver como es esto"
"""""

def diaDeHoy(request):
    dia = datetime.now()
    texto = f"Este template fue creado <br> {dia}"
    return HttpResponse(texto)

def probandoplantilla(self):
    nom = "Diego"
    ap = "Rebora"
    diccionario = {"nombre": nom, "apellido": ap}
    mihtml = open(r"C:\Users\bogac\Codigos\django\sistema_coder\sistema_coder\planatillas\template.html")
    plantilla = Template(mihtml.read())
    mihtml.close()
    micontexto = Context(diccionario)
    documento = plantilla.render(micontexto)
    return HttpResponse(documento)

def todojunto(self):
    nom = "Diego"
    ap = "Rebora"
    dia = datetime.now()
    diccionario = {"nombre": nom, "apellido": ap, "ahora": dia}
    mihtml = open(r"C:\Users\bogac\Codigos\django\sistema_coder\sistema_coder\planatillas\template.html")
    plantilla = Template(mihtml.read())
    mihtml.close()
    micontexto = Context(diccionario)
    documento = plantilla.render(micontexto)
    return HttpResponse(documento)

def plantillaconlista(self): ##SIRVE A SU VEZ PARA BUCLES Y CONDICIONALES, VER TEMPLATE. 
    nom = "Diego"
    ap = "Rebora"
    listaDeNotas = [2, 4, 7, 4, 8]
    dia = datetime.now()
    diccionario = {"nombre": nom, "apellido": ap, "ahora": dia, "notas": listaDeNotas}
    mihtml = open(r"C:\Users\bogac\Codigos\django\sistema_coder\sistema_coder\planatillas\template.html")
    plantilla = Template(mihtml.read())
    mihtml.close()
    micontexto = Context(diccionario)
    documento = plantilla.render(micontexto)
    return HttpResponse(documento)

def saludar_con_html(request):
    contexto = {}
    http_responde = render(
        request=request,
        template_name= r"C:\Users\bogac\Codigos\django\sistema_coder\ControlEstudio\templates\ControlEstudio\base.html",
        context=contexto,
    )
    return http_responde
    


