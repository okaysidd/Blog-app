from django.db import models
from django.urls import reverse
from users_app.models import Author_model
import datetime
from django.utils import timezone


# Create your models here.
class Post_model(models.Model):
    author = models.ForeignKey(Author_model, on_delete=models.CASCADE)
    title_original = models.CharField(max_length=200)
    # title_original means the title at the current state, that will be visible to users
    title_edited = models.CharField(max_length=200, default="")
    # title_edited means the history, the title that was saved first time while creating the blog
    body_original = models.TextField()
    body_edited = models.TextField(default="")
    created_on = models.DateTimeField(auto_now_add=True)
    created_on = models.DateTimeField(default=timezone.now())
    modified_on = models.DateTimeField(blank=True, null=True)
    published_on = models.DateTimeField(blank=True, null=True)
    likes = models.PositiveIntegerField(default=0)
    liked_by = models.ManyToManyField(Author_model, related_name="liked_by", blank=True, null=True, default=[])

    def get_absolute_url(self):
        return reverse('blogs:post', kwargs={'pk':self.pk})

    def publish(self):
        self.published_on = timezone.now()
        self.save()

    def like_post(self, liked_by_user):
        if Author_model.objects.filter(author_name=liked_by_user):
            if Author_model.objects.filter(author_name=liked_by_user)[0] not in self.liked_by.all():
                self.liked_by.add(Author_model.objects.filter(author_name=liked_by_user)[0])
                self.likes += 1
                self.save()
            else:
                self.liked_by.remove(Author_model.objects.filter(author_name=liked_by_user)[0])
                self.likes -= 1
                self.save()

    def __str__(self):
        return self.title_original


class Comment_model(models.Model):
    post = models.ForeignKey(Post_model, on_delete=models.CASCADE)
    author = models.ForeignKey(Author_model, on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text
