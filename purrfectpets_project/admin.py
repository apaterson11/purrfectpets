from django.contrib import admin
from purrfectpets_project.models import Pet,PetPhoto,Comment

# Category is not shown as we do not want any level of user editting it

admin.site.register(Pet)

admin.site.register(PetPhoto)

admin.site.register(Comment)