from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def saludo(request):
    saludo = "SALUDO"
    pagina_html = HttpResponse(saludo)
    return pagina_html
