from django.views.generic import ListView
from django.shortcuts import render , redirect
from .models import productmodel , categories , ModelCommentProduct , subcategories  , subsubcategories
from Blog.forms import CommentForm
from django.contrib.auth.decorators import login_required , user_passes_test
from django.http import HttpResponse
from django.db.models import Q


class index(ListView):
    model = productmodel
    template_name = 'shop/shop.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'products'  # Default: object_list
    paginate_by = 10
    # queryset = productmodel.objects.all()  # Default: Model.objects.all()
    def get_queryset(self):  
        query = productmodel.objects.all()
        object_list = productmodel.objects.filter(deleted=False)
        return object_list


        
class SearchResultsView(ListView):
    model = productmodel
    template_name = "search.html"

    def get_queryset(self):  
        query = self.request.GET.get("result")
        object_list = productmodel.objects.filter(
            Q(ProductName__icontains=query) 
            | Q(category__name=query)
            | Q(category__url_name=query)
        )
        return object_list




def ProductDetailsView(req ,namecate ,namepro):
    cate = categories.objects.get(url_name=namecate)
    if productmodel.objects.get(slug = namepro , category=cate):
        pro = productmodel.objects.get(slug = namepro, category=cate)
        same_pro = productmodel.objects.filter(category=cate,deleted=False)
        commentobject = ModelCommentProduct.objects.filter(accepted = True , post = pro)
        comment_count = commentobject.count()
        context = {'p':pro,'same_pro':same_pro , 'com':commentobject , 'c_count':comment_count}
        return render(req , 'shop/product-details.html' ,context )
    else:
        return redirect("H404")




def commentView(request , proname):
    user = request.user
    comment = CommentForm(request.POST or None)
    context = {"fc":comment }
    if request.method == "POST":
        if comment.is_valid():
            use = user
            name = comment.cleaned_data['name']
            email = comment.cleaned_data['email']
            content = comment.cleaned_data['content']
            pro = productmodel.objects.get(slug = proname)
            promother = pro
            comment = ModelCommentProduct.objects.create( user= use ,name = name,email = email , content = content , post = promother )
            if comment.name and comment.email and comment.content != None:
                comment.save()
                return redirect('productview' ,pro.category.url_name ,pro )
    return render(request, 'blog/newcomment.html' , context)

def categoryView(req , categoriese):
    if categories.objects.filter(url_name = categoriese):
        cat = categories.objects.filter(url_name = categoriese)
        for i in cat:
            o = i.id
            pro = productmodel.objects.filter(category = o, deleted=False)
            return render(req , 'shop/shop.html' , {'products':pro} )
    else:
        return redirect("H404")

def subcategoryView(req , category,subcategory):
    if subcategories.objects.filter(url_name=subcategory) and categories.objects.get(url_name = category):
        cat = categories.objects.get(url_name = category)
        sub = subcategories.objects.filter(url_name=subcategory)
        n = cat.id
        for i in sub:
            o = i.id
            pro = productmodel.objects.filter(sub_categories = o,category=n , deleted=False)
            return render(req , 'shop/shop.html' , {'products':pro} )
    else:
        return redirect("H404")
    

def subsubcategoryView(req , category,subcategory,subsubcategory):
    if subsubcategories.objects.filter(url_name=subsubcategory) and subcategories.objects.filter(url_name=subcategory) and categories.objects.get(url_name = category):
        cat = categories.objects.get(url_name = category)
        sub = subcategories.objects.filter(url_name=subcategory)
        subsub = subsubcategories.objects.filter(url_name=subsubcategory)
        n = cat.id
        for x in sub:
            o = x.id
            for i in subsub:
                c = i.id
                pro = productmodel.objects.filter(sub_sub_categories=c,sub_categories = o,category=n , deleted=False)
                return render(req , 'shop/shop.html' , {'products':pro} )
    else:
        return redirect("H404")

