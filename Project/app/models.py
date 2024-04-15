from django.db import models

from django.db import models

class AdminDataBase(models.Model):
    FirstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    Email=models.EmailField()
    Contact=models.IntegerField()
    Password=models.CharField(max_length=10)
    Image=models.FileField(null=True, upload_to='adminmyimage')
    def __str__(self):
        return self.FirstName + " " +self.lastName
    
class UserDataBase(models.Model):
    FirstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    Email=models.EmailField()
    Contact=models.IntegerField()
    Password=models.CharField(max_length=10)
    Image=models.FileField(null=True,upload_to='adminmyimage')
    def __str__(self):
        return self.FirstName + " " +self.lastName


class EnquiryDataBase(models.Model):
    Studentname=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Contact=models.IntegerField()
    Enquiry=models.TextField()
    def __str__(self):
        return self.Studentname
    

