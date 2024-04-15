from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()

def __str__(self):
    return self.name


class Registration(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)

def __str__(self):
    return self.firstname

