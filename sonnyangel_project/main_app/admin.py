from django.contrib import admin

# Register your models here.
from .models import Sonnyangel, Feeding, Accessories

admin.site.register(Sonnyangel)
admin.site.register(Feeding)
admin.site.register(Accessories)