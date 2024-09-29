from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    phoneNumber = models.CharField(max_length=100, null=True)
    intrest = models.CharField(max_length=100, null=True)
    ratings = models.BigIntegerField(default=0, null=True)
    ratingList = models.JSONField(default=[], null=True)
    views = models.BigIntegerField(default=0, null=True)
    viewList = models.JSONField(default=[], null=True)
    uploads = models.BigIntegerField(default=0, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    bookMarkList = models.JSONField(default=[], null=True)
    chatList = models.JSONField(default=[], null=True)

    def __str__(self):
        return self.name


class File(models.Model):
    uploadedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=500)
    file = models.FileField(upload_to='documents/')
    uploadedAt = models.DateTimeField(auto_now_add=True)
    rating = models.BigIntegerField(default=0, null=True)
    views = models.BigIntegerField(default=0, null=True)
    downloads = models.BigIntegerField(default=0, null=True)
    
    def __str__(self):
        return f"{self.name} : {self.uploadedBy.name}"


class ChatGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)
    createdOn = models.DateTimeField(default=datetime.now)
    displayName = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    chatGroup = models.ForeignKey(ChatGroup, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    message = models.CharField(max_length=1000)

    def __str__(self):
        return f"Message from {self.sender.name} in {self.chatGroup.name}"
