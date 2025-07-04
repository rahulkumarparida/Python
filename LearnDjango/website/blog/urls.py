from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index , name='index'),
    path('<int:blog_id>/' , views.details, name='details'),
    path('addBlog/' , views.addBlog , name ='addBlog')
    
] + static(settings.MEDIA_URL , document_root= settings.MEDIA_ROOT)
