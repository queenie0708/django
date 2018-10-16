"""NBBSWT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include,re_path

from SWT import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^menu/', views.menu,name='menu'),
    url(r'^jsMenu/', views.jsMenu,name='jsMenu'),
    url(r'^prj/(?P<pk>\d+)/$', views.get_Prj, name='get_Prj'),
    url(r'^dropdown/', views.dropdown,name='dropdown'),
    re_path(r'^ajax/load_versions/$', views.ajax_load_versions, name='ajax_load_versions'),
    re_path(r'^ajax/load_results/$', views.ajax_load_results, name='ajax_load_results'),
]
