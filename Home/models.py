from operator import truediv
from django.contrib.auth.models import User
from django.db import models
from django_resized import ResizedImageField
import os
import random
# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext
def upload_image_path_slider_photo(instance, filename):
    new_name = random.randint(1, 27634723542)
    name, ext = get_filename_ext(filename)
    final_name = f"slider--{filename}"
    return f"Slider/{final_name}"

class HomeSliderPhotoModel(models.Model):
    text1 = models.CharField(max_length=100,verbose_name='متن اسلایدرن 1',null=True , blank=True)
    text2 = models.CharField(max_length=100,verbose_name='متن 2',null=True , blank=True)
    text3 = models.CharField(max_length=100,verbose_name='متن 3',null=True , blank=True)
    text4 = models.CharField(max_length=100,verbose_name='متن 4',null=True , blank=True)

    image = models.ImageField(upload_to = upload_image_path_slider_photo , null=True , blank=True,verbose_name = 'عکس')
    class Meta:
        verbose_name = 'عکس اسلایدر صفحه خانه'
        verbose_name_plural = 'عکس های اسلایدر صفحه خانه'

class ModelContact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    title = models.CharField(max_length=300)
    content = models.TextField(max_length=1000)
    class Meta:
        verbose_name = 'ارتباط با ما'
        verbose_name_plural = 'ارتباط با ما'

    

