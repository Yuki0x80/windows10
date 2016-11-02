# -*- coding: utf-8 -*-
"""
Definition of views.
"""

from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.models import Check_list

def list_tasks(request):
    #entities = table_service.query_entities('mytasks', '', 'name,category')
    entities = Check_list.objects.all()
    html = render_to_string('app/test.html', {'entities':entities})     
    return HttpResponse(html)


def add_task(request):     
    name = request.GET['name']     
    category = request.GET['category']
    Check_list.objects.update_or_create(name=name,category=category)
    entities = Check_list.objects.all()   
    html = render_to_string('app/test.html', {'entities':entities})     
    return HttpResponse(html)


def update_task(request):   
    name = request.GET['name']     
    category = request.GET['category']
    Check_list.objects.filter(name=name,category=category).delete()           
    entities = Check_list.objects.all()
    html = render_to_string('app/test.html', {'entities':entities})     
    return HttpResponse(html)
