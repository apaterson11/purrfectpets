from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User



class Category(models.Model):
    NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    views = models.IntegerField(default=0)
    slug = models.SlugField()
    
    types = [
        ('DO', 'Dog'),
        ('CA', 'Cat'),
        ('FI', 'Fish'),
        ('RE', 'Reptile'),
        ('RO', 'Rodent'),
        ('OT', 'Other'),
    ]
    
    animalType = models.CharField(max_length=2, choices=types, default = 'OT')
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.animalType)
        super(Category, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
        
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)     #line is required, links UserProfile to a User model instance
    
    email = models.CharField(unique=True,max_length=128, null=True)
    
    def __str__(self):
        return self.user.username
 
class Pet(models.Model):            
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='', null=True)
    MAX_LENGTH = 128
    owner = models.ForeignKey(User,on_delete=models.CASCADE, related_name="owner", null=True)
    name = models.CharField(max_length=MAX_LENGTH, null=True)
    breed = models.CharField(max_length=MAX_LENGTH, null=True)
    bio = models.TextField(max_length=1000, null=True)
    
    views = models.IntegerField
    
    types = [
        ('DO', 'Dog'),
        ('CA', 'Cat'),
        ('FI', 'Fish'),
        ('RE', 'Reptile'),
        ('RO', 'Rodent'),
        ('OT', 'Other'),
    ]
    animalType =  models.CharField(max_length=2, choices=types, default = 'OT')
    
    awwSenders = models.ManyToManyField(User, related_name="awwSenders",blank = True)
    
    awwCount = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class PetPhoto(models.Model):

    pet = models.ForeignKey(Pet, on_delete = models.CASCADE, related_name="pet", parent_link = True)
    
    photo = models.ImageField(upload_to = 'uploads/')


class Comment(models.Model):
    commentMaker = models.ForeignKey(User,on_delete = models.CASCADE,parent_link=True, null=True)
    commentAbout = models.ForeignKey(Pet,on_delete = models.CASCADE, parent_link=True, null=True)

    timeDate = models.DateTimeField(null=True)
    comment = models.TextField(null=True)
    
    