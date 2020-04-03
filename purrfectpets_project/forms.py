from django import forms
from purrfectpets_project.models import Pet, Comment, Category, PetPhoto
from django.contrib.auth.models import User


class PetForm(forms.ModelForm):
    name = forms.CharField(max_length=Pet.MAX_LENGTH, help_text="Please enter your pet's name.", required=True)
    
    types = [
        ('dogs', 'Dog'),
        ('cats', 'Cat'),
        ('fish', 'Fish'),
        ('reptiles', 'Reptile'),
        ('rodents', 'Rodent'),
        ('others', 'Other'),
    ]
 
    category = forms.ModelChoiceField(help_text = "Please enter the category of your pet.", queryset = Category.objects.all())
    breed = forms.CharField(max_length=Pet.MAX_LENGTH, help_text="Please enter the breed of your pet.", required=True)
    bio = forms.CharField(max_length=1000, help_text="Tell us about your pet!")
    photos = forms.ImageField(required=False, help_text="Enter a photo of your pet")
    awws = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(label="Please enter the category for your pet." ,widget=forms.HiddenInput(), required=False)
    
    class Meta:         #provides additional info on the form
        model = Pet
        fields = ('name','category','breed','bio','photos')
        
class EditAccountForm(forms.ModelForm):
    username = forms.CharField(max_length=150, help_text="Edit the text to change your username.")
    email = forms.EmailField(max_length=320, help_text="Edit the text to change your email.")
    
    class Meta:
        model = User
        fields = ('username', 'email')
        
 
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
        
class PetPhotoForm(forms.ModelForm):
    photo = forms.ImageField()
    class Meta:
        model = PetPhoto
        fields = ('photo',)

class CommentForm(forms.ModelForm):
    body = forms.CharField()

    #Form only takes input for the body variable 

    class Meta:
        model = Comment
        fields = ('body',)




