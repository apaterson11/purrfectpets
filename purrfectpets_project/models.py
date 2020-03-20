from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    email = models.CharField(unique=True,max_length=128)

    def __str__(self):
        return self.user.username


class Pet(models.Model):
    MAX_LENGTH = 128
    owner = models.ForeignKey(UserProfile,on_delete=models.CASCADE, parent_link=True, related_name="owner")
    name = models.CharField(max_length=MAX_LENGTH)
    breed = models.CharField(max_length=MAX_LENGTH)
    animalType = models.CharField(max_length=MAX_LENGTH)
    bio = models.TextField(max_length=1000)
    photos = []

    def addPhoto(self, image):
        photos = photos + [models.ImageField()]
    
    awwSenders = models.ManyToManyField(UserProfile, related_name="awwSenders")
    awwCount = models.IntegerField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    commentMaker = models.ForeignKey(UserProfile,on_delete = models.CASCADE,parent_link=True)
    commentAbout = models.ForeignKey(Pet,on_delete = models.CASCADE, parent_link=True)

    timeDate = models.DateTimeField()

    comment = models.TextField()