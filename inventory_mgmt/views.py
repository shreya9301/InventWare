from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from .forms import StockCreateForm,StockSearchForm
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
		queryset = Stock.objects.filter(category__icontains=form['category'].value(),
										item_name__icontains=form['item_name'].value())
		context = {
		"form": form,
		"header": header,
		"queryset": queryset,
		}
	return render(request, "list_item.html", context)

def add_items(request):
	form = StockCreateForm(request.POST or None)
	if form.is_valid():
	    form.save()
	context = {
		"form": form,
		"title": "Add Item",
	}
	return render(request, "add_items.html", context)