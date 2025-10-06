from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=255)
    city=models.CharField(max_length=70)
    roll=models.IntegerField()
    state=models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class UserLogin(models.Model):
    firstname = models.CharField(max_length=50,default='unknown')
    lastname = models.CharField(max_length=50,default='unknown')
    contactdetail = models.CharField(max_length=15,default='nothing')
    email = models.EmailField(default='null')
    username = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class LoginAuth(models.Model):
    username = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username