# from django.conf.urls import url
from django.urls import path

from .views import BookCreateView, PenerbitListView, IndexClassView

urlpatterns = [
    path('', IndexClassView.as_view()),
    path('create/', IndexClassView.as_view(template='book/form.html'), name='create'),
    path('edit/<int:id>', IndexClassView.as_view(template='book/form.html'), name='edit'),
    # path('', views.index),
    # path('index', views.index, name='index'),
    # path('add/', views.formAdd, name='add'),
    # path('edit/<int:id>', views.formEdit, name='edit'),
    # path('store/', views.store, name='simpan'),
    # path('update/<int:id>', views.update, name='update'),
    # path('delete/<int:id>', views.delete, name='hapus'),
]