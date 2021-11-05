from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['name','slug','body']
    prepopulated_fields = {'slug': ('name',)} 


admin.site.register(Post, PostAdmin)
