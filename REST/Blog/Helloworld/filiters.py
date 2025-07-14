import django_filters
from django import forms

from Helloworld.models import Post




class PostFilter(django_filters.FilterSet):
    created_on = django_filters.DateTimeFilter(widget=forms.DateInput(attrs={'type':'date'}) , lookup_expr='date')
    
    class Meta:
        model = Post
        fields = ['created_on',]