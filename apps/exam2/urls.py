from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('add',views.show),
    path('create',views.create),
    path('join',views.join),
    path('destination/<id>',views.dest),
]