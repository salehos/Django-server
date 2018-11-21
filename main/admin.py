from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from main.models import Food, Reserve


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'create_date', 'image_tag')
    list_filter = ('create_date',)
    search_fields = ('name', 'description', 'create_date')


admin.site.register(Food, FoodAdmin)


@admin.register(Reserve)
class ReserveAdmin(admin.ModelAdmin):
    list_display = ['user', 'food', 'Reserve_date', 'type']
    list_filter = ['user', 'food', 'type', 'Reserve_date']

