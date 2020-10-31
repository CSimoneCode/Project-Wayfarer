from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=50)
    current_city = models.CharField(max_length=100)
    join_date = models.DateField(auto_now_add=True)
    past_cities = models.TextField(blank=True)

    def __str__(self):
        return self.name

