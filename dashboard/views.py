from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm
# Create your views here.

@login_required(login_url = 'account:login')
def index(request):
    return render(request , 'dashboard/index.html')

@login_required(login_url = 'account:login')
def staff(request):
    return render(request , 'dashboard/staff.html')

@login_required(login_url = 'account:login')
def product(request):
    count = 1
    items = Product.objects.all() # Using ORM
    # items = Product.objects.raw('SELECT * FROM dashboard_product')

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(request.path)
    else:
        form = ProductForm()

    context = {
        'items':items,
        'form':form,
        'count':count
    }
    return render(request , 'dashboard/product.html',context)

@login_required(login_url = 'account:login')
def order(request):
    return render(request , 'dashboard/order.html')


@login_required(login_url = 'account:login')
def product_delete(request , pk):
    item = Product.objects.get(id = pk)
    if request.method == 'POST':
        item.delete()
        return redirect("dashboard:product")
    return render(request , 'dashboard/product_delete.html')

@login_required(login_url = 'account:login')
def product_update(request , pk):
    item = Product.objects.get(id = pk)
    if request.method == "POST":
        form = ProductForm(request.POST , instance=item)

        if form.is_valid():
            form.save()
            return redirect ("dashboard:product")
    else:
        form = ProductForm(instance=item)
    context = {
        'form':form
    }
    return render(request , "dashboard/product_update.html",context)