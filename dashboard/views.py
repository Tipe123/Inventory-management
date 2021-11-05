from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product , Order
from .forms import ProductForm ,OrderForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

@login_required(login_url = 'account:login')
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    workers_count = User.objects.all().count()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.staff= request.user
            post.save()
            return redirect('dashboard:index')
    else:
        form = OrderForm()

    context = {
        'orders': orders,
        'form': form,
        'products': products,
        'workers_count': workers_count
    }
    return render(request, 'dashboard/index.html', context)
    

@login_required(login_url = 'account:login')
def staff(request):
    workers = User.objects.all()
    workers_count = User.objects.all().count()
    
    context = {
        'workers': workers,
        'workers_count': workers_count,
    }
    
    return render(request, 'dashboard/staff.html', context)

@login_required(login_url = 'account:login')
def staff_detail(request, pk):
    worker = User.objects.get(id = pk)
    context = {
        'worker': worker
    }
    return render(request, 'dashboard/staff_detail.html', context) 

 
@login_required(login_url = 'account:login')
def product(request):
    count = 1
    items = Product.objects.all() # Using ORM
    # items = Product.objects.raw('SELECT * FROM dashboard_product')
    workers_count = User.objects.all().count()

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added!')
            
            return redirect(request.path)
    else:
        form = ProductForm()

    context = {
        'items':items,
        'form':form,
        'count':count,
        'workers_count': workers_count
    }
    return render(request , 'dashboard/product.html',context)



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

@login_required(login_url = 'account:login')
def order(request):
    orders = Order.objects.all()
    workers_count = User.objects.all().count()
    context = {
        'orders':orders,
        'workers_count': workers_count,
    }
    return render(request , 'dashboard/order.html',context)
