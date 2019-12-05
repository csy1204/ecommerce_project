from django.contrib import admin

# Register your models here.
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display=['id','pw','name','classification','is_staff']
    list_filter=['classification']
    search_fields=['id','name']


admin.site.register(User, UserAdmin)