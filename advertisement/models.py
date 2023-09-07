from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import validate_comma_separated_integer_list 
import random
import os
from taggit.managers import TaggableManager
from django_resized import ResizedImageField

User = get_user_model()

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_name = random.randint(1, 27634723542)
    name, ext = get_filename_ext(filename)
    # final_name = f"{new_name}{ext}"
    final_name = f"{new_name}-{instance.Slug}{ext}"
    return f"Advertisement/{instance.writer}/{final_name}"
    

class AdvertisementModel(models.Model):
    writer = models.ForeignKey(User , on_delete=models.CASCADE,verbose_name = 'نویسنده')
    AdvertisementTitle = models.CharField(max_length=200,verbose_name = 'نام مجله')
    Slug = models.SlugField(allow_unicode=True, blank=True , null=True,verbose_name = 'نام انگلیسی')
    AdvertisementImageMain = models.ImageField(upload_to =upload_image_path, blank=True , null=True,verbose_name = 'عکس اصلی')
    AdvertisementImage1 = ResizedImageField(size=[500,300],upload_to = upload_image_path , null=True , blank=True,verbose_name = 'عکس 1')
    AdvertisementImage2 = ResizedImageField(size=[500,300],upload_to = upload_image_path , null=True , blank=True,verbose_name = 'عکس 2')
    AdvertisementImage3 = ResizedImageField(size=[500,300],upload_to = upload_image_path , null=True , blank=True,verbose_name = 'عکس 3')
    AdvertisementImage4 = ResizedImageField(size=[500,300],upload_to = upload_image_path , null=True , blank=True,verbose_name = 'عکس 4')
    AdvertisementImage5 = ResizedImageField(size=[500,300],upload_to = upload_image_path , null=True , blank=True,verbose_name = 'عکس 5')
    Advertisement_Created_At = models.DateTimeField(auto_now_add=True,verbose_name = 'تاریخ ساخت')
    Advertisement_Updated_At = models.DateTimeField(auto_now=True,verbose_name = 'تاریخ ابدیت')
    AdvertisementBody1  = models.TextField(max_length=1200, blank=True , null=True,verbose_name = 'توضیحات 1')
    AdvertisementBody2  = models.TextField(max_length=1700, blank=True , null=True,verbose_name = 'توضیحات 2')
    AdvertisementBody3  = models.TextField(max_length=1700, blank=True , null=True,verbose_name = 'توضیحات 3')
    AdvertisementBody4  = models.TextField(max_length=1200, blank=True , null=True,verbose_name = 'توضیحات 4')
    AdvertisementBody5 = models.TextField(max_length=1200, blank=True , null=True,verbose_name = 'توضیحات 5')
    Advertisementquote = models.TextField(max_length=1200, blank=True , null=True,verbose_name='متن مهم از تبلیغات')
    Advertisementquestion1 = models.CharField(max_length=100, blank=True , null=True,verbose_name='سوال 1')
    Advertisementquestion2 = models.CharField(max_length=100, blank=True , null=True,verbose_name='سوال 2')
    Advertisementquestion3 = models.CharField(max_length=100, blank=True , null=True,verbose_name='سوال 3')
    Advertisementquestion4 = models.CharField(max_length=100, blank=True , null=True,verbose_name='سوال 4')
    Advertisementquestion5 = models.CharField(max_length=100, blank=True , null=True,verbose_name='سوال 5')
    vip = models.BooleanField(default=False, blank=True , null=True,verbose_name='صفحه خانه')
    tags = TaggableManager(verbose_name='هشتگ') 

    def __str__(self):
        return self.AdvertisementTitle
    def getsnippets(self):
        return self.AdvertisementBody1[:220]
    class Meta:
        verbose_name = 'تبلیغ'
        verbose_name_plural = 'تبلیغات'


class ModelComment(models.Model):
    name = models.CharField(max_length=200 , blank=True , null=True,verbose_name='نام')
    email = models.EmailField(verbose_name='ایمیل')
    content = models.TextField(max_length=1000,verbose_name='متن')
    commentposted = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ')
    accepted = models.BooleanField(default=False,verbose_name='تایید')
    motherpost = models.ForeignKey(AdvertisementModel , on_delete=models.CASCADE, blank=True , null=True,verbose_name='محصول مادر')
    def __str__(self):
        return f'تبلیغ مادر: {self.motherpost} '
    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظر ها'
