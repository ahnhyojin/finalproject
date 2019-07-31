from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    title =  models.CharField(max_length=100)
    pub_date=models.DateTimeField('date published')
    image = models.ImageField(upload_to = 'images/', null = True, )
    body = models.TextField(max_length= 500 )
   
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]
    

    