from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^video/', views.clip),
    url(r'^visualization/', views.visualization),
    url(r'^vis/', views.vis),
    url(r'^modeling/', views.modeling),
    url(r'^interior/', views.interior),
    url(r'^exteriors/', views.exteriors),
    url(r'^object_visualization/', views.object_visualization),
    url(r'^plan_work/', views.plan_work),
]
