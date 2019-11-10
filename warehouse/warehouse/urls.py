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
from product.category import createcategory, updatecategory

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",homeview),
    path("create_category/",createcategory),
    re_path("update_category/(?P<pk>[0-9]+)",updatecategory), #updatecategory(req_ob,pk=3)
]
