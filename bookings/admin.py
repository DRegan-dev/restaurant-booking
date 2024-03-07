from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('name', 'slug',)
    search_fields = ['name']
    list_filter = ('created_on',)
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('content',)
# Register your models here.
