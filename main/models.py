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


class Reserve(models.Model):
    TYPE_CHOICE = (
        (1, "lunch"),
        (2, "dinner")
    )
    # food = models.ForeignKey(Food, on_delete=models.CASCADE)
    food = models.ForeignKey('main.Food', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Reserve_date = models.DateField(auto_now_add=True)
    type = models.IntegerField(choices=TYPE_CHOICE, default=1)
