from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.TextField()

    def __str__(self): return self.name

class Post(models.Model):
    title        = models.TextField()
    description  = models.TextField()
    address      = models.TextField(blank=True)
    city         = models.TextField(blank=True)
    region       = models.TextField(blank=True)
    country      = models.TextField()
    user         = models.ForeignKey(User, blank=True, null=True) #temporary
    category     = models.ForeignKey(Category)
    is_completed = models.BooleanField(default=False)
    is_insider   = models.BooleanField(default=False)

    def __str__(self): return self.title

class PeopleGroup(models.Model):
    name        = models.TextField()
    description = models.TextField()
    global_pop  = models.IntegerField()
    percent_unreached = models.IntegerField()

    def __str__(self): return self.name
