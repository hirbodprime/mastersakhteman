from .models import productmodel, categories , subcategories ,subsubcategories

allpro = productmodel.objects.filter(pk__in=[1,2,3,4,5,6,7,8,9,10])
cate = categories.objects.all()
sub = subcategories.objects.all()
subsub = subsubcategories.objects.all()




def GlobalModels(request):
    return { 
            'cat':cate , 'pro':allpro, 'sub':sub, 'subsub':subsub,
        }

