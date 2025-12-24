from django.db import models
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=255)
    city=models.CharField(max_length=70)
    roll=models.IntegerField()
    state=models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class UserRegistration(models.Model):
    firstname = models.CharField(max_length=50,default='John')
    lastname = models.CharField(max_length=50,default='Doe')
    contactdetail = models.CharField(max_length=15,default='xxxxx-xxxxx')
    email = models.EmailField(default='username@exapmle.com')
    username = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class LoginAuth(models.Model):
    username = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author_name = models.CharField(max_length=100)
    video = models.FileField(upload_to='blog_videos/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title