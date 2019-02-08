from django.contrib import admin
from .models import Comment_model, Post_model


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fields = [
        'title_original',
        'body_original',
        'author_name',
    ]
    search_fields = [
        'title_original',
        'body_original',
        'author_name',
    ]

admin.site.register(Comment_model)
admin.site.register(Post_model)
