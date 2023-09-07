from django.urls import path 
from .views import AdvertisementView , AdvertisementDetailView , commentView,AdvertisementView_tag
urlpatterns = [
    path('' , AdvertisementView , name="advertisementview"),
    path('tag/<slug:tag_slug>/',AdvertisementView_tag, name='advertisementview_tag'),
    path('<str:Slug>' , AdvertisementDetailView , name="advertisementdetailview"),
    path('<str:Slug>/comment' , commentView , name="commentview"),
]
