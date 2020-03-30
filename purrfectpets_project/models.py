from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


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


#Comment Section

#Category
"""
class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absoulte_url(self):
        return reverse('purrfectpets:list_of_post_by_category', args=[self.slug])

    def __str__(self):
        return self.name
"""

#Post
class Post(models.Model):
    STATUS_CHOICES = (
        (0,'Draft'),
        (1,'Publish')
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    def get_absoulte_url(self):
        return reverse('purrfectpets:post_detail', args=[self.slug])

    def __str__(self): 
        return self.title

    """
    class Meta:
        ordering = ['-created_on']
    """

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", null=True)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def approved(self):
        self.approved = True
        self.save()

    #def __str__(self):             #cannot return as User must be a User object
        #return self.user

    