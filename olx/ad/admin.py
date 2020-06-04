from django.contrib import admin
from .models import Ad, Category, AdImages

admin.site.register(Ad)
admin.site.register(AdImages)
admin.site.register(Category)