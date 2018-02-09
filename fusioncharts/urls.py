"""fusioncharts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from samples import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
"""

from django.conf.urls import url
from django.contrib import admin
from views import catalogue


from samples import database_example1, database_example2


urlpatterns = [
    url(r'^database-example1/', database_example1.chart, name='chart'),
    url(r'^database-example2/', database_example2.chart, name='chart'),
    
]
