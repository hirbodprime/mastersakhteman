from django.contrib import admin
from .models import ModelContact , HomeSliderPhotoModel

class ModelContactAdmin(admin.ModelAdmin):
    list_display=['name' , 'email' , 'title' , 'content']

class HomeSliderPhotoModelAdmin(admin.ModelAdmin):
    list_display=['text1' , 'text2' , 'text3' , 'text4', 'image']


admin.site.register(ModelContact , ModelContactAdmin)

admin.site.register(HomeSliderPhotoModel , HomeSliderPhotoModelAdmin)
