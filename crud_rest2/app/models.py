from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)
    phone = models.IntegerField()
    
    