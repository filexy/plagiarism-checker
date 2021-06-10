# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .forms import *
from .models import *
from django.core.paginator import Paginator
from django.shortcuts import render
from datetime import datetime


@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

def file_uploader_view(request):

    msg = None
    if request.method == "POST":
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():   
            form.save()
            msg = 'User created.' 
            return redirect("/documents/repository/")

        else:
            msg = 'Form is not valid' 
    else:
        form =UploadFileForm()

    return render(request, "uploader.html", {"form": form, "msg" : msg  })

def checker_view(request):

    msg = None
    if request.method == "POST":
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():   
            form.save()
            msg = 'User created.' 
            return redirect("/plagiarism/results/")

        else:
            msg = 'Form is not valid' 
    else:
        form =UploadFileForm()

    return render(request, "checker.html", {"form": form, "msg" : msg  })


def uploads_view(request):
    uploads=Uploads.objects.all()
    paginator = Paginator(uploads,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,"uploads.html",{'page_obj': page_obj})

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
