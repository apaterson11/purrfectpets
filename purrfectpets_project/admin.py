from django.contrib import admin
from purrfectpets_project.models import Pet, Comment, Category, PetPhoto
#Register your models here.


admin.site.register(Pet)
admin.site.register(Comment)
admin.site.register(PetPhoto)
admin.site.register(Category)