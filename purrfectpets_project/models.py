from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User



class Category(models.Model):
    views = models.IntegerField(default=0)
    slug = models.SlugField(blank = True)
    
    types = [
        ('DO', 'Dog'),
        ('CA', 'Cat'),
        ('FI', 'Fish'),
        ('RE', 'Reptile'),
        ('RO', 'Rodent'),
        ('OT', 'Other'),
    ]
    
    animalType = models.CharField(max_length=2, choices=types, primary_key = True, default = 'OT')
    
    def save(self, *args, **kwargs):
        for t in self.types:
            if t[0] == self.animalType:
                name = t[1]
        self.slug = slugify(name)
        super(Category, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.slug
        
 
class Pet(models.Model):            
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default='OT', null=True)
    MAX_LENGTH = 128
    owner = models.ForeignKey(User,on_delete=models.CASCADE, related_name="owner", null=True)
    name = models.CharField(max_length=MAX_LENGTH, null=True)
    breed = models.CharField(max_length=MAX_LENGTH, null=True)
    bio = models.TextField(max_length=1000, null=True)
    
    views = models.IntegerField
    
    awwSenders = models.ManyToManyField(User, related_name="awwSenders",blank = True)
    
    awwCount = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class PetPhoto(models.Model):

    pet = models.ForeignKey(Pet, on_delete = models.CASCADE, related_name="pet", parent_link = True, null=True)
    
    photo = models.ImageField(upload_to = 'uploads/', null=True)


class Comment(models.Model):
    commentMaker = models.ForeignKey(User,on_delete = models.CASCADE,parent_link=True, null=True)
    commentAbout = models.ForeignKey(Pet,on_delete = models.CASCADE, parent_link=True, null=True)

    timeDate = models.DateTimeField(null=True)
    comment = models.TextField(null=True)
    
    