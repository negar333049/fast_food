from django.contrib import admin
from .models import Post
# Register your models here.
class postAdmin(admin.ModelAdmin):
    list_display=('title' , 'slug' , 'publish' , 'status')
    list_filter=('publish' , 'status')
    search_fields=('title' , 'description')
    ordering=['status' , 'publish']

admin.site.register(Post, postAdmin)