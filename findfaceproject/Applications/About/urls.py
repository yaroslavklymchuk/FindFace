from django.conf.urls import url, include
from django.contrib import admin
from findfaceproject.Applications.About import views

urlpatterns = [
    url(r'^', views.ResponseForAbout)
]
