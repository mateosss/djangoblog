#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Entrada(models.Model):
    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering=['-fecha']
    
    titulo = models.CharField(u'Título', max_length=100)
    fecha = models.DateTimeField(u'Fecha del Post',auto_now_add=True)
    parallax = models.TextField(u'Imagen del Parallax', default = "{% static 'img/default.jpg' %}")
    contenido = models.TextField(u'Contenido')
    resumen = models.CharField(u'Resumen',max_length=140, default = "resumenossio")
    autor = models.ForeignKey(User)
    
    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering=['-fecha']
    nombre = models.CharField(u'Nombre', max_length=100)
    fecha = models.DateTimeField(u'Fecha',auto_now_add=True)
    mensaje = models.TextField(u'Mensaje')
    entrada = models.ForeignKey(Entrada)

    
    def __str__(self):
        resumen = ""
        extra = ""
        if len(self.mensaje) > 10:
            res = 10
            extra = "..."
        else:
            res = len(self.mensaje)
        for i in range(res):
            resumen += self.mensaje[i]
        return self.nombre + " : " + resumen + extra