
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Web App Endpoints
    path('students/' , include('students.urls')),
    path('employee/' , include('employee.urls')),



    # Api endpoints
    path('api/v1/' , include('api.urls')),



]
