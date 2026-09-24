from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    place = models.CharField(max_length=100)


class StudentDetail(models.Model):
    name = models.CharField(max_length=100)
    valid = models.BooleanField(default=False)
    image = models.ImageField(upload_to='student/')
 
