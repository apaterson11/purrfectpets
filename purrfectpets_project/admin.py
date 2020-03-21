from django.contrib import admin
from purrfectpets_project.models import UserProfile, Pet, Comment, PetPhoto
#Register your models here.


admin.site.register(UserProfile)
admin.site.register(Pet)
admin.site.register(Comment)
admin.site.register(PetPhoto)