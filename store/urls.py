from django.urls import path
from . import views;

app_name="store"

    #path('',views.products_list,name="products_list"),
    #path('<slug:slug>/',views.products_list,name='products_list_by_category'),
    #path('<int:IdArticulo_id>/<slug:slug>/',views.product_detail,name='product_detail'),
   # path('<str:id_categoryLike>',views.products_list,name='products_list_like_category'),

urlpatterns = [
    path('search/', views.products_list_like, name='products_list_like_search'),  # Búsqueda por nombre
    path('category/<slug:slug>/', views.products_list, name='products_list_by_category'),  # Filtrado por categoría
    path('like/<str:id_categoryLike>/', views.products_list, name='products_list_like_category'),  # Categorías similares
    path('product/<int:IdArticulo_id>/<slug:slug>/', views.product_detail, name='product_detail'),  # Detalle del producto
    path('', views.products_list, name="products_list"),  # Lista de productos
]
