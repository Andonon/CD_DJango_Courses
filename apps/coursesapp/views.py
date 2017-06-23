# -*- coding: utf-8 -*-
#pylint: disable=E1101
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Courses
# Create your views here.
def index(request):
    '''home page, has courses list on it'''
    print "1"*50
    print Courses.objects.all()
    # print Courses.objects.all().delete()
    print "1"*50
    context = {
        "courses": Courses.objects.all()
    }
    return render(request, 'coursesapp/index.html', context)

def addcourse(request):
    ''' add course route, for processing db request '''
    print "8"*50
    print request.POST
    print "8"*50
    Courses.objects.create(
        course_name=request.POST['course_name'],
        description=request.POST['course_description']
    )
    return redirect('/')
