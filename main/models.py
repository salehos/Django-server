from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class Food(models.Model):
    name = models.CharField(max_length=128 , default="food")
    description = models.CharField(max_length=512)
    create_date = models.DateTimeField(auto_now_add=True)
    pictue = models.FileField(blank=True , null=True , upload_to="static/food_pics/")

    def image_tag(selfs):
        return mark_safe("<img src='%S' style='max-width:250px ; height = auto'/>" % selfs)