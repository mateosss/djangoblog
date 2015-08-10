
from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse
from models import Entrada, Comentario
from django.core.mail import EmailMessage
import json
import os
def home(request):
    context = RequestContext(request)
    return render_to_response('index.html', 
                              context)

def blog(request):
    context = RequestContext(request)
    posts = Entrada.objects.all()
    return render_to_response('blog.html', 
                              {'posts':posts},
                              context)
def calculadora(request):
    context = RequestContext(request)
    return render_to_response('calculadora.html', 
                              context)
def cronometro(request):
    context = RequestContext(request)
    return render_to_response('cronometro.html', 
                              context)
def conversor(request):
    context = RequestContext(request)
    return render_to_response('conversor.html', 
                              context)
def galeria(request):
    context = RequestContext(request)
    return render_to_response('galeria.html', 
                              context)
def botonfalso(request):
    context = RequestContext(request)
    return render_to_response('botonfalso.html', 
                              context)
def curriculum(request):
    context = RequestContext(request)
    return render_to_response('curriculum.html', 
                              context)
def contacto(request):
    context = RequestContext(request)
    if request.method == 'POST':
        nombre = request.POST['nombre']
        number = request.POST['number']
        mail = request.POST['mail']
        mensaje= request.POST['mensaje']
        email = EmailMessage(nombre+' te ha enviado un mail Mayo', 'Numero: '+number+"\n"+'Mail: '+mail+"\n\n"+mensaje, to=['mateodemayo@gmail.com'])
        email.send()        
    return render_to_response('contacto.html', 
                              context)
def comentar(request):
    context = RequestContext(request)        
    if request.method == 'POST':        
        nombre = request.POST['nombre']
        mensaje = request.POST['mensaje']   
        id_post = request.POST['id']
        comentario = Comentario()
        comentario.mensaje = mensaje        
        comentario.nombre = nombre
        comentario.entrada = Entrada.objects.get(id=id_post)
        comentario.save()
        comentarioReturn = {"nombre": comentario.nombre, "fecha": "Ahora", "mensaje":comentario.mensaje}
    	return HttpResponse(json.dumps(comentarioReturn), content_type="application/json")
	return None	
    
def verPost(request, id_post):
    context = RequestContext(request)    
    mi_post = Entrada.objects.get(id=id_post)
    comentarios = Comentario.objects.filter(entrada=id_post)
    return render_to_response('post.html', 
                                  {'post':mi_post,
                                   'comentarios':comentarios},
                                  context)
