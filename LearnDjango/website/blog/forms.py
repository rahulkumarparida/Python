from blog.models import PostBlog    
from django import forms

class BlogForm(forms.ModelForm):
    class Meta:
        model = PostBlog
        fields = [
            'title' , 'image' ,  'contents'
        ]