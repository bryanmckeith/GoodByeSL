#!/usr/bin/python
# encoding=utf8

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings

def selauger(request):
    return render(request, 'myapp/selauger.html', locals())

def seloger(request):
    return render(request, 'myapp/seloger.html', locals())

def aurevoir(request):
    return render(request, 'myapp/au-revoir.html', locals())

def merci(request):
    return render(request, 'myapp/merci.html', locals())

def rendezvous(request):
    return render(request, 'myapp/rendez-vous.html', locals())