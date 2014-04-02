from django.db import models

# Create your models here.
class NewStory(model.Models):
  title = models.CharField(max_length=30)