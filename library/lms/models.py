from asyncio.windows_events import NULL
from re import T
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,default=NULL)
    name=models.CharField(max_length=20)
    enrollment=models.IntegerField()

    def __str__(self):
        return self.user.first_name+'['+str(self.enrollment)+']'
    @property
    def get_name(self):
        return self.user.first_name
    @property
    def getuserid(self):
        return self.user.id
class book(models.Model):
    book_name=models.CharField(max_length=30)
    isbn=models.IntegerField()
    author=models.CharField(max_length=20)

    def __str__(self):
        return str(self.book_name)+"["+str(self.isbn)+']'
  
class issuedbook(models.Model):
    isbn=models.CharField(max_length=30)
    enrollment=models.CharField(max_length=30) 

    def __str__(self):
        return self.enrollment