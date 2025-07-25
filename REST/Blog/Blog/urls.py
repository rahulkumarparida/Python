"""
URL configuration for Blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path , include
from Helloworld.views import Hello , PostView
from rest_framework import routers



urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/' , Hello.as_view()),
    path('api-auth/', include('rest_framework.urls'))
]
router = routers.SimpleRouter()
router.register('post', PostView , basename='post')
urlpatterns += router.urls 