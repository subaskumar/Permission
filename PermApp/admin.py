from django.contrib import admin
from .models import Blog
# Register your models here.

class AdminBlog(admin.ModelAdmin):
    list_display = ['title','body']
admin.site.register(Blog,AdminBlog)