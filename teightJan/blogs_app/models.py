from django.db import models
from django.urls import reverse
from users_app.models import Author_model


# Create your models here.
class Post_model(models.Model):
    author = models.ForeignKey(Author_model, on_delete=models.CASCADE)
    title_original = models.CharField(max_length=200)
    title_edited = models.CharField(max_length=200, blank=True, null=True)
    body_original = models.TextField()
    body_edited = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    published_on = models.DateTimeField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('blogs:post', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title_original


class Comment_model(models.Model):
    post = models.ForeignKey(Post_model, on_delete=models.CASCADE)
    author = models.ForeignKey(Author_model, on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text
