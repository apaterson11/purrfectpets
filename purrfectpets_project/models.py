from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


# There is no UserProfile Model as all the fields that we require a user
# to have are already met by User


# This Model keeps track of which pets are in each Category
# and how many views a category of pets has had

# All the Categories are made during the set-up population and users
# can never edit them
class Category(models.Model):
    name = models.CharField(max_length=250)
    views = models.IntegerField(default=0)
    slug = models.SlugField(max_length=250, unique=True)
    
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
        print(name)
        if name == 'fish' or name == 'other':
            self.slug = slugify(name)
        else:
            self.slug = slugify(name + 's')
        super(Category, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absoulte_url(self):
        return reverse('purrfectpets:list_of_post_by_category', args=[self.slug])

    
    def __str__(self):
        return self.slug
        
 

# This is the key model as it holds nearly all information associated with each pet
# Each pet has a ManyToOne relationship with a user and a category

# Pets also have a store of how many times they have been Aww'ed and a ManyToMany 
# field with all users who have already sent an Aww
class Pet(models.Model):            
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default='OT', null=True)
    MAX_LENGTH = 128
    owner = models.ForeignKey(User,on_delete=models.CASCADE, related_name="owner", null=True)
    name = models.CharField(max_length=MAX_LENGTH, null=True)
    breed = models.CharField(max_length=MAX_LENGTH, null=True)
    bio = models.TextField(max_length=1000, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField(max_length = MAX_LENGTH, unique = True)

    views = models.IntegerField(default=0)
    
    awwSenders = models.ManyToManyField(User, related_name="awwSenders",blank = True)
    
    awwCount = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Pet, self).save(*args, **kwargs)


# PetPhoto being its own model allows it to have a ManyToOne relationshap with Pet
# Allowing users to add more than one image of their pet if they wish
class PetPhoto(models.Model):

    pet = models.ForeignKey(Pet, on_delete = models.CASCADE, related_name="pet", parent_link = True, null=True)
    
    photo = models.ImageField(upload_to = 'uploads/')


# Comment model has a ManyToOne relationship with both users and pets
# It allows multiple users to comment on multiple pets irrespectively
class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(User,on_delete=models.CASCADE, related_name="commenter", null=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    #The most recent comments are displayed first 
    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)

    