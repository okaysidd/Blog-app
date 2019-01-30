from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class Author_model(models.Model):
    author_name = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    git = models.URLField(max_length=128, blank=True)
    profile_pic = models.ImageField(default='default.jpeg', upload_to='profile_pics')

    def get_absolute_url(self):
        return reverse('users:view-profile', kwargs={'pk':self.pk})

    def __str__(self):
        return str(self.author_name)

    def save(self):
        super().save()

        img = Image.open(self.profile_pic.path)
        if img.height>300 or img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)
