from django.urls import path
from . import views;

app_name="store"

urlpatterns = [
    path('',views.products_list,name="products_list"),
    path('<slug:slug>/',views.products_list,name='products_list_by_category'),
    path('<int:IdArticulo_id>/<slug:slug>/',views.product_detail,name='product_detail'),
    path('<str:id_categoryLike>',views.products_list,name='products_list_like_category'),
]
