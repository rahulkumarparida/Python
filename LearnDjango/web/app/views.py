from django.shortcuts import render , redirect
from app.forms import ContactForm

# Create your views here.

def index(request):
    
    return render(request , 'layouts/index.html' )

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else: 
        CF = ContactForm()
        return render(request , 'layouts/contact.html', {'form': CF})