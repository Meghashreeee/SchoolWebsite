from django.db import models
from django.utils import timezone


class Content(models.Model):
    Name=models.CharField(max_length=100,primary_key=True)
    content=models.TextField()
    def __str__(self):
        return self.Name+" "+self.content

class Announcement(models.Model):
    announcement=models.TextField()
    date = models.DateField(default=timezone.now)
    def __str__(self):
        return self.announcement+" "+str(self.date)

class faculty(models.Model):
    name=models.CharField(max_length=100)
    position=models.CharField(max_length=100,default="Teacher")
    image=models.ImageField(upload_to='faculty',default="default.jpeg")
    def __str__(self):
        return self.name

class Events(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='events')
    about=models.TextField(default="Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatibus deleniti praesentium a porro ea unde ex laborum beatae nulla modi?")
    def __str__(self):
        return self.name