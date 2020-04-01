from django import forms
from purrfectpets_project.models import Pet, Comment, Category
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
 
    breed = forms.CharField(max_length=Pet.MAX_LENGTH, help_text="Please enter the breed of your pet.", required=True)
    bio = forms.CharField(max_length=1000, help_text="Tell us about your pet!")
    photos = []
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    awws = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:         #provides additional info on the form
        model = Pet
        fields = ('name','category','breed','bio',)
 
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','body')




