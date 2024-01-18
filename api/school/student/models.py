from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender =models.CharField(max_length=20)
    phone =models.BigIntegerField()
    email =models.CharField(max_length=30)
    password =models.CharField(max_length=20)
    
    class Meta:
        db_table= 'student_tb'