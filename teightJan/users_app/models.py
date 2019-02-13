from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class Author_model(models.Model):
    author_name = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    git = models.URLField(max_length=128, blank=True)
    profile_pic = models.ImageField(default='default.jpeg', upload_to='profile_pics')
    # followed_by = models.ManyToManyField('self', related_name="followed_by", blank=True, null=True, default=[])

    # if have to have relationship to same model, use 'self' - in quotes
    following = models.ForeignKey('self', related_name="following-authors+", blank=True, null=True, on_delete='SET_NULL')
    following_number = models.PositiveIntegerField(default=0)
    
    # followers_number = models.PositiveIntegerField(default=0)

    def get_absolute_url(self):
        return reverse('users:view-profile', kwargs={'pk':self.pk})

    def follow_user(self, follow_author):
        if Author_model.objects.filter(author_name=follow_author) and Author_model.objects.filter(author_name=follow_author)[0].author_name != self.author_name:
            if Author_model.objects.filter(author_name=follow_author)[0] not in self.following.all():
                self.following.add(Author_model.objects.filter(author_name=follow_author)[0])
                self.following_number += 1
                self.save()
            else:
                self.following.remove(Author_model.objects.filter(author_name=follow_author)[0])
                self.following_number -= 1
                self.save()

    def __str__(self):
        return str(self.author_name)

    def save(self):
        super().save()

        img = Image.open(self.profile_pic.path)
        if img.height>300 or img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)
