"""djangocrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('blog/', include('blog.urls')),
    path('', index),
    # path('media/', include('media_app.urls')),
    # path('music/', include('Music.urls')),
    # path('book/', include('book.urls')),
    # path('penerbit.php/', PenerbitListView.as_view()),
    path('penerbit.php/', include('book.urls')),
    path('produk.php/', include('produk.urls')),
    path('pelanggan/', include('pelanggan.urls'))
]
