from django.db import models

# Create your models here.
class Testimonials(models.Model):
    image_url = models.CharField(max_length=2083)
    count     = models.CharField(max_length=255)
    name      = models.CharField(max_length=200)

class Slider(models.Model):
    name = models.CharField(max_length=255)
    details = models.CharField(max_length=300) 

class UserDetailsForm(models.Model):
    user_name  = models.CharField(max_length=200)
    user_email = models.CharField(max_length=200)
    user_phone_number = models.IntegerField(max_length=15)
    user_message = models.CharField(max_length=300)
