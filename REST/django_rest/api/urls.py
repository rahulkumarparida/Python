from django.urls import path , include
from api import views

urlpatterns = [
    path('students/' , views.studentsView , name='students'),
    path('students/<int:pk>' , views.studentDetailview , name='StudentDetails'),

    # Employee api endpoints
    path('employee/' , views.Employee.as_view()), 
    path('employee/<int:pk>' , views.employeeDetail.as_view() , name='EmployeeDetails'),
]