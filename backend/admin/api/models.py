from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    phoneNumber = models.CharField(max_length=100, null=True)
    intrest = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.name

class File(models.Model):
    uploadedBy = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=500)
    file = models.FileField(upload_to='documents/')
    uploadedAt = models.DateTimeField(auto_now_add=True)
    rating=models.CharField(max_length=100,null=True)
    views=models.CharField(max_length=100,null=True)
    downloads=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.name +" : "+ self.uploadedBy.name