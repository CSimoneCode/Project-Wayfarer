from django.contrib import admin
from .models import Profile, Posts, City, Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Posts)
admin.site.register(City)
admin.site.register(Comment)
