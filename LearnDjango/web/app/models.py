from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=30)
    Email = models.EmailField()
    content = models.TextField(max_length=250)
        
    
    