from django import forms
from purrfectpets_project.models import Pet, Comment, UserProfile
from django.contrib.auth.models import User

class PetForm(forms.ModelForm):
    owner = forms.ForeignKey(widget=forms.HiddenInput(), intial=owner)
    name = forms.CharField(max_length=Pet.MAX_LENGTH, help_text="Please enter your pet's name.")
    animalType = forms.CharField(max_length=Pet.MAX_LENGTH, help_text="Please enter the type of animal your pet is.")
    breed = forms.CharField(max_length=Pet.MAX_LENGTH, help_text="Please enter the breed of your pet.")
    bio = forms.TextField(max_length=1000, help_text="Tell us about your pet!")
    photos = []
    
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    awws = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        
        if url and not url.startswith('http://'):       # If url is not empty and doesn't start with 'http://' then prepend 'http://'
            url = f'http://{url}'
            cleaned_data['url'] = url
            
        return cleaned_data
    
    class Meta:         #provides additional info on the form
        model = Pet
        fields = ('owner','name','animalType','breed','bio',)
        
class CommentForm(forms.ModelForm):
    commentMaker = forms.ForeignKey(widget=forms.HiddenInput())           #don't know what to put here?
    commentAbout = forms.ForeignKey(widget=forms.HiddenInput())
    timeDate = forms.DateTimeField(widget=forms.HiddenInput())
    comment = forms.TextField(max_length=1000, help_text="What do you think?")
        
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('email',)