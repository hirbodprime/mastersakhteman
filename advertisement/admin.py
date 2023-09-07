from django.contrib import admin
from .models import AdvertisementModel,ModelComment



admin.site.register(ModelComment)
admin.site.register(AdvertisementModel)