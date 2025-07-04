from django.db import models

# Create your models here.
class PostBlog(models.Model):
    title = models.CharField()
    image = models.ImageField(upload_to='images/')
    time = models.DateTimeField(auto_now_add=True)
    contents = models.TextField()     
    
    def summary(self):
        return self.contents[:40]
    
    def date(self):
        return self.time.strftime('%d %e, %y ')
    
    def __str__(self):
        return self.title