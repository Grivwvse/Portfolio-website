from django.db import models

class Person(models.Model):
    fullName = models.CharField(max_length=255)
    about = models.TextField()
    post = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photos/")

class Projects(models.Model):
    preson = models.ForeignKey(Person,on_delete=models.CASCADE)
    projName = models.CharField(max_length=255)
    description = models.TextField()
    link = models.TextField()

class Skills(models.Model):
    preson = models.ForeignKey(Person,on_delete=models.CASCADE)
    skiName = models.TextField()

class Experience(models.Model):
    preson = models.ForeignKey(Person,on_delete=models.CASCADE)
    comName = models.TextField()
    post = models.CharField(max_length=255)
    dateStart = models.DateField()
    dateEnd = models.DateField()

class Education(models.Model):
    preson = models.ForeignKey(Person,on_delete=models.CASCADE)
    eduName = models.TextField()
    eduDepartment = models.TextField(default='IT')
    eduQualification = models.TextField(default='IT')
    dateStart = models.DateField()
    dateEnd = models.DateField()