from django.contrib import admin
from.models import *

# admin customization
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_show','title','url','date')
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','url')
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 30

#  if i cnage admin them then tinymce wala chalane k liye

    # class Media:
    #     js = ('js/script.js',)

# Registr your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post,PostAdmin)