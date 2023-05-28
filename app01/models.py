from django.db import models


# Create your models here.
class UserList(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    remark = models.CharField(max_length=100, default='', blank=True)
    age = models.IntegerField(max_length=4, null=True, blank=True)