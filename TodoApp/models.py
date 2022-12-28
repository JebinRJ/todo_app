from django.db import models
from django.contrib.auth.models import User




class UserProfile(models.Model):


    name = models.CharField(max_length=200)
    image = models.ImageField(null=True,blank=True,upload_to='images/')
    email = models.EmailField()
    bio = models.TextField(max_length=500)

class CreateTodo(models.Model):

    todo = models.TextField('Enter Todo', max_length=1000)

    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status_choices = [
        ('C','Completed'),
        ('P','Pending'),
    ]
    status = models.CharField(max_length=2,choices=status_choices)




# Create your models here.
