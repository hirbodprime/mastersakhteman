from django.shortcuts import redirect, render
from .models import AdvertisementModel , ModelComment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from taggit.models import Tag
from django.shortcuts import  get_object_or_404


def AdvertisementView_tag(req , tag_slug=None):
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        Advertisement = AdvertisementModel.objects.filter(tags__in=[tag])
        return render(req , 'Advertisement/Advertisement.html',{'advertisement':Advertisement , 'tag':tag_slug})
    else:
        return redirect("H404")

def AdvertisementView(req):
    Advertisement = AdvertisementModel.objects.all()
    return render(req , 'Advertisement/Advertisement.html',{'advertisement':Advertisement})

def AdvertisementDetailView(req , Slug):
    try:
        Advertisement = AdvertisementModel.objects.get(Slug = Slug)
        tags = Tag.objects.filter(advertisementmodel=Advertisement.id)
        commentobject = ModelComment.objects.filter(accepted = True , motherpost = Advertisement)
        return render(req , 'Advertisement/Advertisement-details.html' , {'b':Advertisement ,'tags':tags, 'com':commentobject})
    except Exception as e: 
        return redirect("H404")
    


def commentView(request , Slug):
    comment = CommentForm(request.POST or None)
    context = {"fc":comment}
    if request.method == "POST":
        if comment.is_valid():
            name = comment.cleaned_data['name']
            email = comment.cleaned_data['email']
            content = comment.cleaned_data['content']
            Advertisement = AdvertisementModel.objects.get(Slug = Slug)
            Advertisementmothere = Advertisement
            comment = ModelComment.objects.create( name = name,email = email , content = content , motherpost = Advertisementmothere )
            if comment.name and comment.email and comment.content != None:
                comment.save()
                return redirect('advertisementdetailview' ,Advertisement )
    return render(request, 'Advertisement/newcomment.html' , context)
