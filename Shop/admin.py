from django.contrib import admin
from . import models as md



# Register your models here.
class ProductModeladmin(admin.ModelAdmin):
    fieldsets = [
        ('اطلاعات فروشنده' , {'fields':['Seller','ProductName' ,'slug' ]}),
        ('عکس های محصول' , {'fields':['image' , 'image2', 'image3', 'image4', 'image5']}),
        ('اطلاعات اصلی محصول' , {'fields':['Dimensions','ProductBody' , 'ProductBody2' , 'price_type1', 'price_type2', 'price_type3', 'count']}),
        ('دسته بندی محصول ها' , {'fields':['category','sub_categories','sub_sub_categories' ]}),
        ('اطلاعات وان و جکوزی' , {'fields':['HowMany','OptionsList','OptionsWithJaccuzi','OptionsWithOne' , 'Weight' , 'WaterWeight']}),
        ('دیگر اطلاعات' , {'fields':['deleted' , 'firstpage' , 'Tags']})
    ]
    list_display= ['ProductName','deleted','id' ,  'Seller' , 'date' ,'category']
    search_fields=['id']

class categoriesAdmin(admin.ModelAdmin):
    list_display= [ 'name' , 'url_name','id']

class sub_categoriesAdmin(admin.ModelAdmin):
    list_display= [ 'name' ,'url_name' , 'id']

class sub_sub_categoriesAdmin(admin.ModelAdmin):
    list_display= [ 'name' ,'url_name' , 'id']
admin.site.register(md.ModelCommentProduct)
admin.site.register(md.productmodel ,ProductModeladmin)
admin.site.register(md.categories , categoriesAdmin)
admin.site.register(md.subcategories,sub_categoriesAdmin)
admin.site.register(md.subsubcategories,sub_sub_categoriesAdmin)