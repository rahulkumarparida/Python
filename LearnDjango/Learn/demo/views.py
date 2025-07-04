from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Hello(request):
    return HttpResponse('Hello World from me ')

def helloHtml(request):
    return render(request , 'index.html' , {'name': 'Rahul' , 'age':21 })

def biodata(request):
    name = request.POST['Name']
    age = request.POST['Age']
    DateofBirth = request.POST['DateofBirth']
    
    data = {'name':name ,'age':age,'dob': DateofBirth}

    return render(request , 'biodata.html' , data)