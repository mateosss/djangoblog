
from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse
from models import Entrada, Comentario
from django.core.mail import EmailMessage
import json
import os
#from blog.models import Entrada, Contacto, Comentario
# Create your views here.
def home(request):
    context = RequestContext(request)
    #os.system("zenity --info --text  \"holis"+"pepe"+"\"")
    #posts = Entrada.objects.all()
    #posts = Entrada.objects.filter(published = True)
    return render_to_response('index.html', 
                              #{'posts':posts},
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
                              #{'posts':posts},
                              context)
def cronometro(request):
    context = RequestContext(request)
    return render_to_response('cronometro.html', 
                              #{'posts':posts},
                              context)
def conversor(request):
    context = RequestContext(request)
    return render_to_response('conversor.html', 
                              #{'posts':posts},
                              context)
def galeria(request):
    context = RequestContext(request)
    return render_to_response('galeria.html', 
                              #{'posts':posts},
                              context)
def botonfalso(request):
    context = RequestContext(request)
    return render_to_response('botonfalso.html', 
                              #{'posts':posts},
                              context)
def curriculum(request):
    context = RequestContext(request)
    return render_to_response('curriculum.html', 
                              #{'posts':posts},
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
        os.system("zenity --info --text  \"holis"+comentario.nombre+"\"")                
        comentarioReturn = {"nombre": comentario.nombre, "fecha": comentario.fecha, "mensaje":comentario.mensaje}
    #return render_to_response('post.html',{'comentario':comentarioReturn},context)
    return HttpResponse(json.dumps(comentarioReturn), content_type="application/json")

def verPost(request, id_post):
    context = RequestContext(request)    
    mi_post = Entrada.objects.get(id=id_post)
    comentarios = Comentario.objects.filter(entrada=id_post)
    return render_to_response('post.html', 
                                  {'post':mi_post,
                                   'comentarios':comentarios},
                                  context)
