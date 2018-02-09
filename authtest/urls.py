
#!python
# authtest/urls.py
from django.conf.urls import include, url
from django.contrib import admin
# Add this import
from django.contrib.auth import views
from log.forms import LoginForm

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('log.urls')),
    url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/login'}), 
    url(r'^home/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),

    url(r'^survey/', include('multilingual_survey.urls', namespace="survey")),
    url(r'^register/', include('users.urls', namespace="users")), 
    url(r'^graph/', include('fusioncharts.urls', namespace="graph")), 


]
