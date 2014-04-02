from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NewStory(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()
  pub_date = models.DateTimeField('date published')
  author = models.ForeignKey(User)
  