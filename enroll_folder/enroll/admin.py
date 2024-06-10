from django.contrib import admin
from .models import user
# Register your models here

@admin.register(user)
class useradmin(admin.ModelAdmin):
    list =('id','name','email','password')
