from django.db import models

class Room(models.Model):
    Number_of_room = models.IntegerField()
    Type_of_room = models.IntegerField()

    def __str__(self):
        return self.Number_of_room

class users(models.Model):
    email =models.TextField(max_length=50)
    password =models.CharField(max_length=20)
    role =models.IntegerField()
