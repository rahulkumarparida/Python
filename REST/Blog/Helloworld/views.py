from django.shortcuts import render
from rest_framework.response import  Response
from rest_framework.decorators import APIView  
from Helloworld.serializer import PostSerializer
from rest_framework.viewsets import ModelViewSet
from Helloworld.models import Post
from rest_framework.permissions import IsAuthenticated
from Helloworld.permissions import IsPostProcessor
from rest_framework import filters
from Helloworld.filiters import PostFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.



class PostView(ModelViewSet):
    permission_classes = [IsAuthenticated , IsPostProcessor]
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend ,filters.SearchFilter , filters.OrderingFilter ]
    filterset_class = PostFilter
    search_fields = ['title' , 'content']
    ordering_fields = ['id']
    
    def get_queryset(self):
        return Post.objects.filter(created_by = self.request.user)
    
    
    
Hllo = {
    'msg' : 'Hello World',
    'names' : ['Rahul', 'Situ' , 'Chikun' , 'Dinesh'],
    'food' : ['Anthing with Chicken' , 'Chowmien' , 'Chicken Biryani**'],
    'age': 21,
    'Singularity' : True
}

class Hello(APIView):
    def get(self , request):
         return Response(Hllo)
