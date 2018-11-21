from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from main.models import Food


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'create_date', 'image_tag')
    list_filter = ('create_date', )
    search_fields = ('name', 'description', 'create_date')


admin.site.register(Food, FoodAdmin)
