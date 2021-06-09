# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from .views import *


urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
  
    path('files/add/', file_uploader_view, name="uploader"),
    path('documents/repository/', uploads_view, name="uploads"),
    re_path(r'^.*\.*', views.pages, name='pages'),

]
