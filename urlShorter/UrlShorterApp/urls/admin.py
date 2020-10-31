from django.contrib import admin
from .models import Url
# Register your models here.
@admin.register(Url)
class UrlAdminClass(admin.ModelAdmin):
    fields = ['user_url', 'slug', 'user']