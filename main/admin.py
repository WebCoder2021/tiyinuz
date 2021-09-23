from django.contrib import admin
from .models import NewsType, Category, New
# Register your models here.
admin.site.register(NewsType)
admin.site.register(Category)
admin.site.register(New)
