from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    title='Welcome to Inventware'
    context = {
        "title":title
    }
    return render(request,"home.html",context)

@login_required	
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

@login_required
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

def stock_detail(request, pk):
	queryset = Stock.objects.get(id=pk)
	context = {
		"title": queryset.item_name,
		"queryset": queryset,
	}
	return render(request, "stock_detail.html", context)	

def issue_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = IssueForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.quantity -= instance.issue_quantity
		instance.issue_by = str(request.user)
		messages.success(request, "Successfully Issued ! " + str(instance.quantity) + " " + str(instance.item_name) + "s now left in Store")
		instance.save()

		return redirect('/stock_detail/'+str(instance.id))
		# return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": 'Issue ' + str(queryset.item_name),
		"queryset": queryset,
		"form": form,
		"username": 'Issue By: ' + str(request.user),
	}
	return render(request, "add_items.html", context)



def receive_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = ReceiveForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.quantity += instance.receive_quantity
		instance.save()
		messages.success(request, "Successfully Recieved ! " + str(instance.quantity) + " " + str(instance.item_name)+"s now in Store")

		return redirect('/stock_detail/'+str(instance.id))
		# return HttpResponseRedirect(instance.get_absolute_url())
	context = {
			"title": 'Reaceive ' + str(queryset.item_name),
			"instance": queryset,
			"form": form,
			"username": 'Receive By: ' + str(request.user),
		}
	return render(request, "add_items.html", context)

def reorder_level(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = ReorderLevelForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Reorder level for " + str(instance.item_name) + " is updated to " + str(instance.reorder_level))

		return redirect("/list_item")
	context = {
			"instance": queryset,
			"form": form,
		}
	return render(request, "add_items.html", context)