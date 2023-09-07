from django.contrib import admin
from .models import BlogModel , ModelComment
# Register your models here.
class BlogModelAdmin(admin.ModelAdmin):
    fieldsets = [
        ('blog owner,title' , {'fields':['writer' ,'BlogTitle','Slug' ]}),
        ('blog body' , {'fields':['BlogImageMain','Blogquestion1' , 'BlogBody1','BlogImage1' ,'Blogquestion2', 'BlogBody2','BlogImage2', 'Blogquestion3','BlogBody3','BlogImage3','Blogquestion4','BlogBody4','BlogImage4','Blogquestion5','BlogBody5','BlogImage5']}),
        ('blog details' , {'fields':['Blogquote' , 'vip'  , 'tags']})
    ]
admin.site.register(BlogModel , BlogModelAdmin)

admin.site.register(ModelComment)
