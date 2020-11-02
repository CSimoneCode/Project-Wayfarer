from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    name = models.CharField(max_length=50)
    current_city = models.CharField(max_length=100)
    join_date = models.DateField(auto_now_add=True)
    past_cities = models.TextField(blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()