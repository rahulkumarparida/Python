
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