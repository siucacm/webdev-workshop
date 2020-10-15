from django.db import models

# Create your models here.
class Quote(models.Model):
  quote_text = models.CharField(max_length=500)
  quote_author = models.CharField(max_length=200)