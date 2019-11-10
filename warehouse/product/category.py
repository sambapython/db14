from django.shortcuts import render
from product.models import Category
def createcategory(request):
	#data = request.GET
	categories =  Category.objects.all()
	if request.method == "POST":
		data=request.POST
		cat = Category(name=data.get("cat_name"))
		cat.save()
	return render(request, "product/createcategory.html",
		{"categories":categories})

def updatecategory(request,pk):
	cat = Category.objects.get(id=pk)
	if request.method == "POST":
		data = request.POST
		cat.name=data.get('cat_name')
		cat.save()
	return render(request,"product/updatecategory.html",{"category":cat})

