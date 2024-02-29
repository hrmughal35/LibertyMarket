from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=300)
    phone=models.CharField(max_length=300)
    email=models.EmailField(max_length=300)
    comments=models.TextField(max_length=500)
