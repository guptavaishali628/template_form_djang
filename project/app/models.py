from django.db import models

# Create your models here.
class Student(models.Model):#table name==student
    Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Contact=models.IntegerField()
    