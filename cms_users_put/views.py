from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import get_template
from django.template import Context

from models import Page


def mostrar(request, resource):
    salida = ""
    if request.user.is_authenticated():
        salida += "<p>Hi " + request.user.username + ". "
        salida += "<a href='/logout/'>Logout</a></p>"
    else:
        salida += "<p>You aren't logged in. "
        salida += "<a href='/admin/login/'>Login!</a></p>"

    if request.method == "GET":
        try:
            fila = Page.objects.get(name=resource)
            salida += fila.page
        except Page.DoesNotExist:
            return HttpResponseNotFound(salida + 'Page not found: ' + resource)

    elif request.method == "PUT":
        if request.user.is_authenticated():
            fila = Page.objects.filter(name=resource)
            if not fila:
                newpage = Page(name=resource, page=request.body)
                newpage.save()
                salida += "New page added:\n" + request.body
            else:
                salida += "That page is in the server"
        else:
            salida += "YOU MUST <a href='/admin/login/'>LOG IN</a>"

    return HttpResponse(salida)


def mostrarPlantilla(request, resource):
    salida = ""
    log = ""
    title = resource
    content = ""
    found = True
    if request.user.is_authenticated():
        log += "<p>Hi " + request.user.username + ". "
        log += "<a href='/logout/'>Logout</a></p>"
    else:
        log += "<p>You aren't logged in. "
        log += "<a href='/admin/login/'>Login!</a></p>"

    if request.method == "GET":
        try:
            fila = Page.objects.get(name=resource)
            content += fila.page
        except Page.DoesNotExist:
            content += '404 Page not found'
            found = False

    elif request.method == "PUT":
        if request.user.is_authenticated():
            fila = Page.objects.filter(name=resource)
            if not fila:
                newpage = Page(name=resource, page=request.body)
                newpage.save()
                content += "New page added:\n" + request.body
            else:
                content += "That page is in the server"
        else:
            salida += "YOU MUST <a href='/admin/login/'>LOG IN</a>"

    plantilla = get_template('index.html')
    cntxt = Context({'TITULO': title, 'CONTENIDO': content, 'LOG': log})
    renderizado = plantilla.render(cntxt)
    if found:
        return HttpResponse(renderizado)
    else:
        return HttpResponseNotFound(renderizado)
