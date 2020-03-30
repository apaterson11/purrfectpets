from django.contrib import admin
from purrfectpets_project.models import Pet, Post, Category, Comment, PetPhoto
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'approved')

admin.site.register(Comment, CommentAdmin)


admin.site.register(Pet)
admin.site.register(PetPhoto)
