from django.contrib import admin
from .models import Vser
# Register your models here.
@admin.register(Vser)
class UserAdmin(admin.ModelAdmin):
    list_dispplay = ('id', 'name', 'password', 'massages')