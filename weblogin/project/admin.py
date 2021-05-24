from django.contrib import admin
from .models import Patient, Oxygen, Plasma
# Register your models here.
admin.site.register(Patient)
admin.site.register(Oxygen)
admin.site.register(Plasma)