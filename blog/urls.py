# from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:id>/<str:type>', views.recent),
    path('ab/', views.ab),
    path('tentangkami/', views.tentangkami),
]