from django.contrib import admin
from .models import Comment_model, Post_model


# Register your models here.
admin.site.register(Comment_model)
admin.site.register(Post_model)
