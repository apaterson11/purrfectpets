from django.contrib import admin
from purrfectpets_project.models import Pet, Category, Comment, PetPhoto
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'pet', 'created_on')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


#admin.site.register(Comment, CommentAdmin)


admin.site.register(Pet)
admin.site.register(PetPhoto)
