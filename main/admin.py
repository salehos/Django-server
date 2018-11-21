from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from main.models import Food
from main.models import User


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'create_date', 'image_tag')
    list_filter = ('create_date',)
    search_fields = ('name', 'description', 'create_date')


admin.site.register(Food, FoodAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'family')
    list_filter = ('name',)
    search_fields = ('name', 'family', 'email')


admin.site.register(User, UserAdmin)

#
# class OrderAdmin(admin.ModelAdmin):
#     pass