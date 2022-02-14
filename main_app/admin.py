from django.contrib import admin

# Register your models here.

from .models import Profile, City, Guide, User

admin.site.register(Profile)
admin.site.register(City)
admin.site.register(Guide)