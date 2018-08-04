from django.urls import path, include
from django.contrib import admin
from product import views

urlpatterns = [
    path('users/', views.UserList.as_view(),name=views.UserList.name),
    path('product/',views.ProductList.as_view(),name=views.ProductList.name),
    path('product/<int:pk>/', views.ProductDetail.as_view(),name=views.ProductDetail.name),
    path('users/<int:pk>/', views.UserDetail.as_view(),name=views.UserDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path('api-auth/', include('rest_framework.urls'))
]
