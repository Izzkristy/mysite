from django.db import models
from datetime import datetime


# Create your models here.
class Guestbook(models.Model):
    nickname = models.CharField(max_length=16, unique=True)
    email = models.EmailField(blank=True, null=True)
    face = models.IntegerField()
    content = models.TextField()
    createtime = models.DateTimeField(default=datetime.now())
    clientip = models.CharField(max_length=15)
    reply = models.TextField(blank=True, null=True)
    replytime = models.DateTimeField(null=True)
