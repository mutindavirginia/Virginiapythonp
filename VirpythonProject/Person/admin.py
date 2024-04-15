from django.contrib import admin
# Register your models here.

from .models import Person, Registration

admin.site.register(Person)
admin.site.register(Registration)