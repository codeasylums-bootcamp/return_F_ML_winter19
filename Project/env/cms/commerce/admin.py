from django.contrib import admin
from .models import Laptop


# Register your models here.

admin.site.site_header = 'returnF - Press F to pay respect'



admin.site.register(Laptop)
