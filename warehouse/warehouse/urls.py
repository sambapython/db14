"""warehouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path
from product.views import homeview
from product.category import createcategory, updatecategory,deletecategory
from django.views.generic import CreateView, UpdateView, DeleteView
from product.models import Product,Transaction
from product.productviews import createproduct, updateproduct, deleteproduct
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",homeview),
    path("create_category/",createcategory),
    re_path("update_category/(?P<pk>[0-9]+)",updatecategory), #updatecategory(req_ob,pk=3)
    re_path("delete_category/(?P<pk>[0-9]+)",deletecategory),
    path("create_product",createproduct),
    re_path("update_product/(?P<pk>[0-9]+)",updateproduct),
    re_path("delete_product/(?P<pk>[0-9]+)",deleteproduct),
    path("create_transaction",CreateView.as_view(
         model=Transaction,
         fields = "__all__",
         success_url="/",
         )),
    re_path("update_transaction/(?P<pk>[0-9]+)",UpdateView.as_view(
        model=Transaction,
         fields = "__all__",
         success_url="/",
        )),
    re_path("delete_transaction/(?P<pk>[0-9]+)",DeleteView.as_view(
        model=Transaction,
        success_url="/",
        ))
]

urlpatterns = urlpatterns+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
