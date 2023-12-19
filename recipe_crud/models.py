from django.db import models

# Create your models here.
class Recipe(models.Model):
    rname = models.CharField(max_length=70)
    rcategory = models.CharField(max_length=50)
    rarea = models.CharField(max_length=50)
    rdrink = models.CharField(max_length=50)
    rinstruction = models.TextField()
    rvideoLink = models.URLField(blank=True,null=True)
