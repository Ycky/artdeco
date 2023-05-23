from django.contrib import admin
from .models import *

@admin.register(Houses)
class HousesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
