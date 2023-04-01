from django.contrib import admin

from main.models import Uploads, Cars, Positions

# Register your models here.
admin.site.register(Cars)
admin.site.register(Uploads)
admin.site.register(Positions)
