from django.conf.urls import url
from . import views
from django.urls import path
                    
urlpatterns = [
    path('', views.index),
    path('create',views.create),
    path('login',views.login),
    
    path('logout',views.logout)
]