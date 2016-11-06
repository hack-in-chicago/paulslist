from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.TextField()

# Create your models here.
class Post(models.Model):
    title        = models.TextField()
    description  = models.TextField()
    user         = models.ForeignKey(User)
    category     = models.ForeignKey(Category)
    is_completed = models.BooleanField()
    is_insider   = models.BooleanField()
