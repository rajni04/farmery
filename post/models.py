
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from tinymce import HTMLField

CustomUser = get_user_model()




class Author(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateTimeField(blank=True)
    comment_count = models.IntegerField(default = 0)
    slug=models.CharField(max_length=130)
    content =HTMLField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    featured = models.BooleanField()
    previous_post = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'pk': self.pk
        })