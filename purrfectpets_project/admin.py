from django.contrib import admin
from purrfectpets_project.models import UserProfile, Pet, Comment
# Register your models here.


admin.site.register(UserProfile)
admin.site.register(Pet)
admin.site.register(Comment)