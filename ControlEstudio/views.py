from django.shortcuts import render

# Create your views here.
def listar_alumnos(request):
    contexto = { 
        "estudiantes" : [ 
        {"nombre": "Diego", "apellido": "Rebora"},
        {"nombre": "Pame", "apellido": "Cantero"},
        {"nombre": "Charly", "apellido": "Huergo"},
            ]
              }

    http_responde = render(
        request=request,
        template_name= "ControlEstudio\lista_estudiantes.html",
        context=contexto,
    )
    return http_responde

