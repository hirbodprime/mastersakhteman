from django.urls import path 
from .views import BlogView , BlogDetailView , commentView,BlogView_tag
urlpatterns = [
    path('' , BlogView , name="blogview"),
    path('tag/<slug:tag_slug>/',BlogView_tag, name='blogview_tag'),
    path('<str:Slug>' , BlogDetailView , name="blogdetailview"),
    path('<str:Slug>/comment' , commentView , name="commentview"),
]
