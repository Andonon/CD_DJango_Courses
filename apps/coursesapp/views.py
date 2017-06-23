# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Courses
# Create your views here.
def index(request):
    print "1"*50
    print Courses.objects.all()
    print "1"*50
    return render(request, 'coursesapp/index.html')

def addcourse(request): 
    print "8"*50
    print request.POST
    print "8"*50
    return redirect('/')