from django.shortcuts import render , redirect
from Shop.models import productmodel , categories
from django.views.generic.edit import CreateView
from .forms import ContactUsForm 
from .models import ModelContact , HomeSliderPhotoModel
from django.http import HttpResponse
from Blog.models import BlogModel
from django.db.models import Count

def HomeView(req):
    home = HomeSliderPhotoModel.objects.all()
    all_categories = categories.objects.all()
    allproducts = productmodel.objects.all()
    jacuzzi_products = productmodel.objects.filter(category=1 , firstpage=True, deleted=False)
    ceramic_products = productmodel.objects.filter(category=2,firstpage=True, deleted=False)
    pr3 = productmodel.objects.filter(category=3,firstpage=True, deleted=False)
    pr4 = productmodel.objects.filter(category=4,firstpage=True, deleted=False)
    blog = BlogModel.objects.filter(vip=True)
    return render(req , 'Home/index.html' , 
        {
        'hsp':home,
        'jp':jacuzzi_products,
        'cp':ceramic_products,
        'pr3':pr3,
        'pr4':pr4,
        'all_cate':all_categories,
        'bg':blog
        }
    )



# class ContactUsView(CreateView):
#     model = ModelContact
#     template_name = 'Home/contact.html'
#     form_class = ContactUsForm
#     success_url = '/'

#     def form_valid(self, form):
#         try:
#             response = super().form_valid(form)
#         except IntegrityError:
#             return HttpResponse("There was an error processing your request.")
        
#         return response


def contactview(request):
    contact = ContactUsForm(request.POST or None)
    context = {"form": contact}
    if request.method == "POST":
            if contact.is_valid():
                name = contact.cleaned_data['name']
                email = contact.cleaned_data['email']
                title = contact.cleaned_data['title']
                content = contact.cleaned_data['content']
                contact = ModelContact.objects.create(name = name  , email = email ,title = title , content = content )
                contact.save()
                return redirect('HomeView')
    return render(request, 'Home/contact.html' , context)


def coming(req):
    return render(req , 'Home/Others/coming-soon.html')
def faq(req):
    return render(req , 'Home/Others/faq.html')
def privacy(req):
    return render(req , 'Home/Others/privacy-policy.html')
def h404(req):
    return render(req , 'Home/HttpErrors/404.html')

def not_found404(req,exception):
    return render(req , 'Home/HttpErrors/404.html',status=404)
def testview(req):
    return render(req , 'Home/tests.html')
def aboutview(req):
    return render(req , 'Home/about.html')


def workwithus(req):
    return render(req , 'Home/workwithus.html')