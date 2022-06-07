from django.db import models

class User(models.Model):
    number=models.TextField(max_length=13,primary_key=True)
    name=models.TextField(max_length=100)

class Message(models.Model):
    user=models.ForeignKey(to=User,on_delete=models.CASCADE)
    message=models.TextField(max_length=1000)
    dateTime=models.DateTimeField(auto_now_add=True)


