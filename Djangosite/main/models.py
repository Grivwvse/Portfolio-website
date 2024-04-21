from django.db import models

class Person(models.Model):
    fullName = models.CharField(max_length=255)
    about = models.TextField()
    timeUpdate = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to="photos/")

class Projects(models.Model):
    Name = models.CharField(max_length=255)
    Desc = models.TextField()
    URL = models.TextField()

