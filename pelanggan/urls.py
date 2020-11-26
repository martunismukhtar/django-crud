# from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('add/', views.formAdd),
    path('edit/<int:id>', views.formEdit),
    # path('store/', views.store),
    # path('update/<int:id>', views.update),
    # path('delete/<int:id>', views.delete),
]