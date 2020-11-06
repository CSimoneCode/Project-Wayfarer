from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.forms import ImageField
import datetime


class Profile(models.Model):
    name = models.CharField(max_length=50)
    current_city = models.CharField(max_length=100)
    join_date = models.DateField(auto_now_add=True)
    past_cities = models.TextField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to="main_app/static/images", null=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=85)
    # photo - via uploadcare? Elias knows what to do 
    country = models.CharField(max_length=85)
    region = models.CharField(max_length=85)
    language = models.CharField(max_length=50, blank=True)
    blurb = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}, {self.country}'


class Posts(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    # hashtags = models.CharField() ### May need middleware for hashtag functionality - doing more research
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} made post {self.title} on {self.post_date}'


class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=300)
    parent_post = models.ForeignKey(Posts, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} made comment {self.title} on {self.post_date}'
