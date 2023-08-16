from django.db import models

# Create your models here.
class studentModel(models.Model):
    name = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    age = models.IntegerField(max_length=3)
    classIn = models.IntegerField(max_length=100)


class registerUser(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    emailId = models.EmailField(max_length=3)
    password = models.CharField(max_length=15)