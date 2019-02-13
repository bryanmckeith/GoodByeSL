#!/usr/bin/python
# encoding=utf8

from django.conf.urls import url
from . import views

urlpatterns = [
    url('selauger', views.selauger, name='selauger'),
    url('seloger', views.seloger, name='seloger'),
    url('au-revoir', views.aurevoir, name='aurevoir'),
    url('merci', views.merci, name='merci'),
    url('rendez-vous', views.rendezvous, name='rendezvous'),
]