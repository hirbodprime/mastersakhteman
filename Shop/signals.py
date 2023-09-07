from django.db.models.signals import post_save , pre_save
from .models import productmodel
# from django.utils.text import slugify
import locale
import os

def ProductModelPriceSignal(sender, instance, **kwargs):
    locale.setlocale(locale.LC_ALL, 'en_US')
    
    PurePrice = locale.format("%d", instance.price_type1, grouping=True)
    instance.show_price = PurePrice
    
    PurePrice2 = locale.format("%d", instance.price_type2, grouping=True)
    instance.show_price2 = PurePrice2
    
    PurePrice3 = locale.format("%d", instance.price_type3, grouping=True)
    instance.show_price3 = PurePrice3
    
    
pre_save.connect(ProductModelPriceSignal, sender=productmodel)



def pre_save_slugify_productmodel(sender , instance , *args, **kwargs):
    if not instance.slug:
        slug = instance.ProductName.replace(' ','-')
        instance.slug = slug
    else:
        if instance.ProductName:
            instance.slug = ''
            slug = instance.ProductName.replace(' ','-')
            instance.slug = slug


pre_save.connect(pre_save_slugify_productmodel ,sender=productmodel)