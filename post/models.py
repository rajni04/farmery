from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()




class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    featured = models.BooleanField()
    
    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'pk': self.pk
        })