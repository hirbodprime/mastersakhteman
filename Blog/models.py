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
    return f"Blogs/{instance.writer}/{final_name}"
    

class BlogModel(models.Model):
    writer = models.ForeignKey(User , on_delete=models.CASCADE,verbose_name = 'نویسنده')
    BlogTitle = models.CharField(max_length=200,verbose_name = 'نام مجله')
    Slug = models.SlugField(allow_unicode=True, blank=True , null=True,verbose_name = 'نام انگلیسی')
    BlogImageMain = models.ImageField(upload_to =upload_image_path, blank=True , null=True,verbose_name = 'عکس اصلی')
    BlogImage1 = ResizedImageField(size=[500,300],upload_to = upload_image_path , null=True , blank=True,verbose_name = 'عکس 1')
    BlogImage2 = ResizedImageField(size=[500,300],upload_to = upload_image_path , null=True , blank=True,verbose_name = 'عکس 2')
    BlogImage3 = ResizedImageField(size=[500,300],upload_to = upload_image_path , null=True , blank=True,verbose_name = 'عکس 3')
    BlogImage4 = ResizedImageField(size=[500,300],upload_to = upload_image_path , null=True , blank=True,verbose_name = 'عکس 4')
    BlogImage5 = ResizedImageField(size=[500,300],upload_to = upload_image_path , null=True , blank=True,verbose_name = 'عکس 5')
    Blog_Created_At = models.DateTimeField(auto_now_add=True,verbose_name = 'تاریخ ساخت')
    Blog_Updated_At = models.DateTimeField(auto_now=True,verbose_name = 'تاریخ ابدیت')
    BlogBody1  = models.TextField(max_length=1200, blank=True , null=True,verbose_name = 'توضیحات 1')
    BlogBody2  = models.TextField(max_length=1700, blank=True , null=True,verbose_name = 'توضیحات 2')
    BlogBody3  = models.TextField(max_length=1700, blank=True , null=True,verbose_name = 'توضیحات 3')
    BlogBody4  = models.TextField(max_length=1200, blank=True , null=True,verbose_name = 'توضیحات 4')
    BlogBody5 = models.TextField(max_length=1200, blank=True , null=True,verbose_name = 'توضیحات 5')
    Blogquote = models.TextField(max_length=1200, blank=True , null=True,verbose_name = 'متن کوتاه مهم از مجله')
    Blogquestion1 = models.CharField(max_length=100, blank=True , null=True,verbose_name = 'سوال 1')
    Blogquestion2 = models.CharField(max_length=100, blank=True , null=True,verbose_name = 'سوال 2')
    Blogquestion3 = models.CharField(max_length=100, blank=True , null=True,verbose_name = 'سوال 3')
    Blogquestion4 = models.CharField(max_length=100, blank=True , null=True,verbose_name = 'سوال 4')
    Blogquestion5 = models.CharField(max_length=100, blank=True , null=True,verbose_name = 'سوال 5')
    vip = models.BooleanField(default=False, blank=True , null=True,verbose_name = 'صفحه خانه')
    tags = TaggableManager(verbose_name = 'هشتگ') 

    def __str__(self):
        return self.BlogTitle
    def getsnippets(self):
        return self.BlogBody1[:220]
    class Meta:
        verbose_name = 'مجله'
        verbose_name_plural = 'مجله ها'

class ModelComment(models.Model):
    name = models.CharField(max_length=200 , blank=True , null=True,verbose_name = 'نام')
    email = models.EmailField(verbose_name = 'ایمیل')
    content = models.TextField(max_length=1000,verbose_name = 'نظر')
    commentposted = models.DateTimeField(auto_now_add=True,verbose_name = 'تاریخ')
    accepted = models.BooleanField(default=False,verbose_name = 'تایید')
    motherpost = models.ForeignKey(BlogModel , on_delete=models.CASCADE, blank=True , null=True,verbose_name = 'پست مادر')
    def __str__(self):
        return f'بلاگ مادر: {self.motherpost} '
    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظر ها'
