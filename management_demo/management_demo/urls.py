"""
URL configuration for managmentdemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # *** products paths ***
    path('products/', views.ProductsView.as_view(), name="products"),
    path('products/<str:product_id>/', views.ProductsView.as_view(), name="products_with_id"),
    # *** helper function paths ***
    path('loadData', views.load_data, name="load_data"),
    path('deleteAllData', views.delete_all_data, name="delete_all_data"),
]
