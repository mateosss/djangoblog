
from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect
from models import Entrada, Comentario
import os
#from blog.models import Entrada, Contacto, Comentario
# Create your views here.
def home(request):
    context = RequestContext(request)
    #os.system("zenity --info --text  \"holis\"")
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
    return render_to_response('contacto.html', 
                              #{'posts':posts},
                              context)
def verPost(request, id_post):
    context = RequestContext(request)    
    mi_post = Entrada.objects.get(id=id_post)
    if request.method == 'POST':
        nombre= request.POST['nombre']
        mensaje= request.POST['mensaje']
        comentario = Comentario()
        comentario.mensaje = mensaje
        comentario.nombre = nombre
        comentario.entrada = mi_post
        comentario.save()
    comentarios = Comentario.objects.filter(entrada=id_post)

    return render_to_response('post.html', 
                                  {'post':mi_post,
                                   'comentarios':comentarios},
                                  context)
