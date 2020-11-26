# from django.conf.urls import url
from django.urls import path

from .views import ProdukList, ProdukCreate, ProdukUpdate, DeleteView
#https://docs.djangoproject.com/en/3.1/topics/class-based-views/generic-editing/
urlpatterns = [
    path('', ProdukList.as_view()),
    path('index', ProdukList.as_view()),
    path('create/', ProdukCreate.as_view(), name='create'),
    path('edit/<int:pk>', ProdukUpdate.as_view(), name='edit'),
    path('delete/<int:pk>', DeleteView.as_view(), name='delete'),
    # path('', views.index),
    # path('index', views.index, name='index'),
    # path('add/', views.formAdd, name='add'),
    # path('edit/<int:id>', views.formEdit, name='edit'),
    # path('store/', views.store, name='simpan'),
    # path('update/<int:id>', views.update, name='update'),
    # path('delete/<int:id>', views.delete, name='hapus'),
]