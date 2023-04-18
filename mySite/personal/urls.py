from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('templates/product_page.html',views.product, name='product'),
    path('templates/personal_info.html',views.info, name = 'info'),
]
