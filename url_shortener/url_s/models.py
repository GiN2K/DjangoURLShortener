from email.policy import default
from django.db import models
from django.forms import CharField, URLField

class Urlmodel(models.Model):
    original_url = models.URLField(max_length=250,default="")
    shortened_url = models.CharField(max_length=15,default="")