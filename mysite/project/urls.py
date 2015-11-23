from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name='index'),
    url(r'^blank', views.blank, name='blank'),
    url(r'^bootstrap-elements', views.bootelement, name='bootelement'),
    url(r'^bootstrap-grid', views.bootgrid, name='bootgrid'),
    url(r'^charts', views.charts, name='charts'),
    url(r'^forms', views.forms, name='forms'),
    url(r'^indexrtl', views.indexrtl, name='indexrtl'),
    url(r'^tables', views.tables, name='tables'),
]