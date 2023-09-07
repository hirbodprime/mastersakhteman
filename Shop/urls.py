from django.urls import path , re_path
from . import views as v


urlpatterns = [
    path('', v.index.as_view(), name="ShopView"),
    path('seach/' , v.SearchResultsView.as_view() , name="search_results"),
    path('<str:categoriese>/' , v.categoryView , name="ProShopView2"),
    path('<str:category>/<str:subcategory>/' , v.subcategoryView , name="subcategoryviewname"),
    path('<str:category>/<str:subcategory>/<str:subsubcategory>/' , v.subsubcategoryView , name="subsubcategoryviewname"),
    path('products/<str:namecate>/<str:namepro>' , v.ProductDetailsView , name="productview"),
    path('products/<str:proname>/comment/' , v.commentView , name="commentviewshop"),
]