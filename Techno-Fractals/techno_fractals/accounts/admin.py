from django.contrib import admin
from accounts.models import UserProfileInfo,Blog

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Blog)