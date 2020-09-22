from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from .forms import StockCreateForm,StockSearchForm,StockUpdateForm
# Create your views here.
def home(request):
    title='Welcome to Inventware'
    context = {
        "title":title
    }
    return render(request,"home.html",context)
def list_item(request):
	form = StockSearchForm(request.POST or None)	
	header = 'CURRENT STOCKS IN THE INVENTORY'

	queryset = Stock.objects.all()
	context = {
		"form": form,
		"header": header,
		"queryset": queryset,
	}
	if request.method == 'POST':
		queryset = Stock.objects.filter(
										item_name__icontains=form['item_name'].value()
										)	
		context = {
		"form": form,
		"header": header,
		"queryset": queryset,
	}								
	return render(request, "list_item.html", context)

def add_items(request):
	form = StockCreateForm(request.POST or None)
	if request.method == 'POST':
		form = StockCreateForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, 'Successfully Saved')
			return redirect('/list_item')
	context = {
		"form": form,
		"title": "Add Item",
	}
	return render(request, "add_items.html", context)

def update_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = StockUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = StockUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			messages.success(request, 'Updated Successfully')
			return redirect('/list_item')

	context = {
		'form':form
	}
	return render(request, 'update_items.html', context)	

def delete_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		messages.success(request, 'Deleted successfully')
		return redirect('/list_item')
	return render(request, 'delete_items.html')	