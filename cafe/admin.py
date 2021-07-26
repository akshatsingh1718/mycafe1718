from django.contrib import admin
from .models import DailyStatement, Sale

# Register your models here.
admin.site.register(Sale)
admin.site.register(DailyStatement)