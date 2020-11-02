from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=50)
    current_city = models.CharField(max_length=100)
    join_date = models.DateField(auto_now_add=True)
    past_cities = models.TextField(blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Posts(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    post_date = models.DateField(auto_now_add=True)
    content = models.TextField(blank=True)
    hashtags = models.CharField() ### May need middleware for hashtag functionality - doing more research
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.profile} made post {self.title} on {self.post_date}'
