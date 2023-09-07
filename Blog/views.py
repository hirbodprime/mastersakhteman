from django.shortcuts import redirect, render
from .models import BlogModel , ModelComment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from taggit.models import Tag
from django.shortcuts import  get_object_or_404


def BlogView_tag(req , tag_slug=None):
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        Blog = BlogModel.objects.filter(tags__in=[tag])
        return render(req , 'blog/blog.html',{'blog':Blog , 'tag':tag_slug})
    else:
        return redirect("H404")

def BlogView(req):
    Blog = BlogModel.objects.all()
    return render(req , 'blog/blog.html',{'blog':Blog})

def BlogDetailView(req , Slug):
    try:
        blog = BlogModel.objects.get(Slug = Slug)
        tags = Tag.objects.filter(blogmodel=blog.id)
        commentobject = ModelComment.objects.filter(accepted = True , motherpost = blog)
        return render(req , 'blog/blog-details.html' , {'b':blog ,'tags':tags, 'com':commentobject})
    except Exception as e: 
        # blog = None
        return redirect("H404")
    


def commentView(request , Slug):
    comment = CommentForm(request.POST or None)
    context = {"fc":comment}
    if request.method == "POST":
        if comment.is_valid():
            name = comment.cleaned_data['name']
            email = comment.cleaned_data['email']
            content = comment.cleaned_data['content']
            blog = BlogModel.objects.get(Slug = Slug)
            blogmothere = blog
            comment = ModelComment.objects.create( name = name,email = email , content = content , motherpost = blogmothere )
            if comment.name and comment.email and comment.content != None:
                comment.save()
                return redirect('blogdetailview' ,blog )
    return render(request, 'blog/newcomment.html' , context)
