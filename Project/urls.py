"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.views.generic import detail

from . import views
from .settings import MEDIA_URL, MEDIA_ROOT
from .views import Main, UploadUser
from django.conf.urls.static import static


urlpatterns = [
    path('', Main.as_view(), name='home'),
    path('', Main.as_view()),
    path('content/upload', UploadUser.as_view()),
    path('detail/<int:id>/', views.detail, name='detail'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)