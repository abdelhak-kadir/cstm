from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(person)
admin.site.register(order)
admin.site.register(order_europ)
admin.site.register(adminstation)
admin.site.register(news)