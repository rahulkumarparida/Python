from django.shortcuts import render , get_object_or_404 , redirect
from blog import models

from blog.forms import BlogForm
# Create your views here.

def index(request):
    post = models.PostBlog.objects
    return render(request , 'layouts/index.html' , {'post': post})


def addBlog(request):
    if request.method == "POST":
        form = BlogForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BlogForm()
        return render(request , 'layouts/addBlog.html', {'form': form} )


def details(request, blog_id):
    detail = get_object_or_404(models.PostBlog ,pk = blog_id)
    return render(request , 'layouts/details.html' , {'post' : detail})