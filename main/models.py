from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class Food(models.Model):
    name = models.CharField(max_length=128, default="food")
    description = models.CharField(max_length=512)
    create_date = models.DateTimeField(auto_now_add=True)
    image = models.FileField(blank=True, null=True, upload_to="static/food_pics/")

    def image_tag(self):
        return mark_safe("<img src='%S' style='max-width:250px ; height = auto'/>" % self.image)


class User(models.Model):
    name = models.CharField(max_length=128)
    family = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    password = models.CharField(max_length=128)


class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
