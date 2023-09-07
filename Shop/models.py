from email.policy import default
from django.db import models
import os
import random
from django.contrib.auth import get_user_model
from django_resized import ResizedImageField
import os
from django_mysql.models import ListCharField
 
User = get_user_model()

ForHowMany = (
    ('یک نفره','یک نفره'),
    ('دو نفره و سه نفره','دو نفره و سه نفره'),
    ('چهار نفره','چهار نفره'),
    ('شش نفره','شش نفره'),
    ('هشت نفره','هشت نفره'),
)


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext
def upload_image_path_category(instance, filename):
    new_name = random.randint(1, 27634723542)
    name, ext = get_filename_ext(filename)
    # final_name = f"{new_name}{ext}"
    final_name = f"category-{instance.url_name}-{filename}"
    return f"Categories/{instance.url_name}/{final_name}"

def upload_image_path_product(instance, filename):
    new_name = random.randint(1, 27634723542)
    name, ext = get_filename_ext(filename)
    # final_name = f"{new_name}{ext}"
    final_name = f"{new_name}-{instance.slug}{ext}"
    return f"Products/{instance.slug}/{final_name}"
    
# def upload_image_path(instance, filename):
#     new_name = random.randint(1, 27634723542)
#     name, ext = get_filename_ext(filename)
#     # final_name = f"{new_name}{ext}"
#     try:
#         if instance.name:
#             final_name = f"category-{instance.name}-{filename}"
#             return f"Categories/{instance.name}/{final_name}"
#     except:    
#         if instance.slug:
#             final_name = f"{new_name}-{instance.slug}{ext}"
#             return f"Products/{instance.slug}/{final_name}"
    

class categories(models.Model):
    name = models.CharField(max_length=50, null=True,blank=True,unique=True,verbose_name = 'نام دسته بندی')
    url_name = models.SlugField(unique=True , null=True , blank=True,allow_unicode=True,verbose_name = 'نام انگلیسی دسته بندی')
    image = ResizedImageField(size=[1920,1920], crop=['top', 'left','bottom', 'right'],upload_to = upload_image_path_category , null=True , blank=True,verbose_name = 'عکس')
    def __str__(self):
        return self.url_name
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

class subcategories(models.Model):
    parent = models.ForeignKey(categories ,blank=True, null=True, on_delete=models.CASCADE,verbose_name = 'دسته بندی پدر')
    name = models.CharField(max_length=50,null=True,blank=True,verbose_name = 'نام زیر دسته بندی')
    url_name = models.SlugField(null=True,blank=True,allow_unicode=True,verbose_name = 'نام زیر دسته بندی انگلیسی')
    def __str__(self):
        return f'{self.parent}-{self.name}'
    class Meta:
        verbose_name = 'زیر دسته بندی'
        verbose_name_plural = 'زیر دسته بندی ها'

class subsubcategories(models.Model):
    parent = models.ForeignKey(subcategories ,blank=True, null=True, on_delete=models.CASCADE,verbose_name = 'دسته بندی پدر')
    name = models.CharField(max_length=100,null=True,blank=True,verbose_name = 'نام زیر زیر دسته بندی')
    url_name = models.SlugField(null=True,blank=True,allow_unicode=True,verbose_name = 'نام زیر زیر دسته بندی انگلیسی')
    def __str__(self):
        return f'{self.parent}-{self.name}'
    class Meta:
        verbose_name = 'زیر زیر دسته بندی'
        verbose_name_plural = 'زیر زیر دسته بندی ها'


class productmodel(models.Model):
    Seller = models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank=True,verbose_name = 'فروشنده') 
    category = models.ForeignKey(categories ,blank=True, null=True, on_delete=models.CASCADE , related_name="categories_main",verbose_name = 'دسته بندی')
    sub_categories = models.ForeignKey(subcategories ,blank=True, null=True, on_delete=models.CASCADE,verbose_name = 'زیر دسته بندی')
    sub_sub_categories = models.ForeignKey(subsubcategories ,blank=True, null=True, on_delete=models.CASCADE,verbose_name = 'زیر زیر دسته بندی')
    ProductName = models.CharField(max_length=60,verbose_name = 'نام محصول')
    slug = models.SlugField(unique=True , null=True , blank=True,allow_unicode=True,verbose_name = 'نام انگلیسی محصول')
    ProductBody = models.TextField(max_length=800, null=True , blank=True,verbose_name = 'توضیحات 1')
    ProductBody2  = models.TextField(blank=True, max_length=300, null=True,verbose_name = 'توضیحات دو')
    image = ResizedImageField(upload_to = upload_image_path_product , null=True , blank=True,verbose_name = 'عکس 1')
    image2 = ResizedImageField(upload_to = upload_image_path_product , null=True , blank=True,verbose_name = 'عکس 2')
    image3 = ResizedImageField(upload_to = upload_image_path_product , null=True , blank=True,verbose_name = 'عکس 3')
    image4 = ResizedImageField(upload_to = upload_image_path_product , null=True , blank=True,verbose_name = 'عکس 4')
    image5 = ResizedImageField(upload_to = upload_image_path_product , null=True , blank=True,verbose_name = 'عکس 5')
    date = models.DateTimeField(auto_now_add=True)
    count = models.PositiveIntegerField(default=0 ,null=True , blank=True,verbose_name = 'تعداد')
    Dimensions = models.CharField(max_length=60,null=True , blank=True,verbose_name = 'چند در چند')
    Weight = models.SmallIntegerField(null=True , blank=True,verbose_name = 'وزن')
    WaterWeight = models.SmallIntegerField(null=True , blank=True,verbose_name = 'مخزن آب')
    HowMany = models.CharField(max_length=60,choices=ForHowMany,null=True , blank=True,verbose_name = 'چند نفره')
    Tags = ListCharField(
        base_field=models.CharField(max_length=50),
        null=True,
        blank=True,
        size=30,
        max_length=(2000) # 6 * 10 character nominals, plus commas
        ,verbose_name = 'هشتگ'
    )
    OptionsList = ListCharField(
        base_field=models.CharField(max_length=50),
        null=True,
        blank=True,
        size=30,
        max_length=(2000) # 6 * 10 character nominals, plus commas
        ,verbose_name = 'امکانات'
    )
    OptionsWithJaccuzi = ListCharField(
        base_field=models.CharField(max_length=50),
        null=True,
        blank=True,
        size=30,
        max_length=(2000) # 6 * 10 character nominals, plus commas
        ,verbose_name = 'امکانات جکوزی'
    )
    OptionsWithOne = ListCharField(
        base_field=models.CharField(max_length=50),
        null=True,
        blank=True,
        size=30,
        max_length=(2000) # 6 * 10 character nominals, plus commas
        ,verbose_name = 'امکانات وان'
    )
    price_type1 = models.PositiveBigIntegerField(null=True , blank=True,verbose_name = 'قیمت تیپ 1')
    price_type2 = models.PositiveBigIntegerField(null=True , blank=True,verbose_name = 'قیمت تیپ 2')
    price_type3 = models.PositiveBigIntegerField(null=True , blank=True,verbose_name = 'قیمت تیپ 3')
    show_price = models.CharField(default="0", blank=True, max_length=30,verbose_name = '')
    show_price2 = models.CharField(default="0", blank=True, max_length=30,verbose_name = '')
    show_price3 = models.CharField(default="0", blank=True, max_length=30,verbose_name = '')
    deleted = models.BooleanField(null=True , blank=True , default=False,verbose_name = 'پاک شود؟')
    firstpage = models.BooleanField(null=True , blank=True , default=False,verbose_name = 'صفحه خانه')
    def __str__(self):
        # return f'ProuctName:{self.ProductName} ProductAuthor:{self.author} ProductId:{self.id}'
        return self.ProductName
    def getsnippet(self):
        return self.ProductBody[0:30]
    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
class ModelCommentProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True , null=True,verbose_name = 'کاربر' )
    name = models.CharField(max_length=200 , blank=True , null=True,verbose_name = 'نام')
    email = models.EmailField(verbose_name = 'ایمیل')
    content = models.TextField(max_length=1000,verbose_name = 'فروشنده')
    commentposted = models.DateTimeField(auto_now_add=True,verbose_name = 'تاریخ')
    accepted = models.BooleanField(default=False,verbose_name = 'تایید؟')
    post = models.ForeignKey(productmodel , on_delete=models.CASCADE, blank=True , null=True,verbose_name = 'محصول')
    def __str__(self):
        return f'محصول مادر: {self.post} '
    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'