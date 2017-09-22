from django.db import models

# Create your models here.
class MyModel(models.Model):
    # AID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,default="123")
    isDel=models.BooleanField(default=True)

class User(models.Model):
    UID=models.AutoField(primary_key=True)
    UName=models.CharField(max_length=40,default="12333")