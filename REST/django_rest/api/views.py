# from django.shortcuts import render
# from django.http import JsonResponse
from students.models import Student
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.serializers import StudentSerializer , EmployeeSerializer

from rest_framework.views import APIView
from employee.models import Employees
from django.http import Http404



# Create Student views here.[OLD method]
@api_view(['GET' , 'POST'])
def studentsView(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET' , 'PUT' , 'DELETE'])
def studentDetailview(request , pk):
    try:
        student = Student.objects.get(pk = pk)
    except Student.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data , status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student , data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':

        student.delete()
        serializer = StudentSerializer(student)
        return Response(serializer.data , status=status.HTTP_204_NO_CONTENT)
    


# Create Employee views here.[New Method]

class Employee(APIView):
    def get(self , request):
        employees = Employees.objects.all()
        serializer = EmployeeSerializer(employees , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    def post(self , request):
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

class employeeDetail(APIView):
    def get_object(self , pk):
        try:
            return Employees.objects.get(pk=pk)
        except Employees.DoesNotExist:

            raise Http404
    def get(self , request , pk):
        emp = self.get_object(pk)
        serilaizer = EmployeeSerializer(emp)
        return Response(serilaizer.data , status=status.HTTP_200_OK)
    
    def put(self , request , pk):
        emp = self.get_object(pk)
        serializer = EmployeeSerializer(emp , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self , request , pk):
        emp = self.get_object(pk)
        emp.delete()
        serilaizer = EmployeeSerializer(emp)
        return Response(serilaizer.data , status=status.HTTP_204_NO_CONTENT)
    