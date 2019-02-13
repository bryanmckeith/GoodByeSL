#!/usr/bin/python
# encoding=utf8

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings

def error404(request):
    return render(request, 'myapp/404.html', locals())