from django.shortcuts import render
from django.http import HttpResponse
from product.models import Category

# Create your views here.
def homeview(request):
	#return HttpResponse("Hello")
	categories = Category.objects.all()
	return render(request,"product/home.html",{"categories":categories})
