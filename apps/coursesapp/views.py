# -*- coding: utf-8 -*-
#pylint: disable=E1101
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Courses

# Create your views here.
def index(request):
    '''home page, has courses list on it'''
    print "home*"*20
    print Courses.objects.all()
    # print Courses.objects.all().delete()
    context = {
        "courses": Courses.objects.all()
    }
    return render(request, 'coursesapp/index.html', context)

def addcourse(request):
    ''' add course route, for processing db request '''
    print "add*"*20
    print request.POST
    Courses.objects.create(
        course_name=request.POST['course_name'],
        description=request.POST['description']
    )
    return redirect('/')

def destroy(request, course_id):
    ''' destroy confirm page, confirm with user '''
    print "Destroy*"*20
    print Courses.objects.all()
    print "Destroy*"*20
    itemtodelete = Courses.objects.get(id=course_id)
    print itemtodelete
    return redirect('/')

def confirmdestroy(request, course_id):
    ''' destroy confirm page, confirm with user '''
    print "ConfirmDestroy*"*20
    print request.POST
    return redirect('/')
