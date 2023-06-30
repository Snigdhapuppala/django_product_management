from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Product, Category

from.forms import ProductForm


from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# To view all the product in the showProducts.html

#@login_required(login_url='accounts/login')
def ShowAllProducts(request):
    category = request.GET.get('category')

    if Category == None:
        products = Product.objects.filter(is_published=True).order_by('-price')  # DB--> Table ->2 records
    else:
        products = Product.objects.filter(category__name=category)
    #  number_of_products = Product.objects.all().count()
    #  print("Number of products is:", number_of_products)

    page_num = request.GET.get('page')
    paginator = Paginator(products, 12)
    try:
        products = paginator.page(page_num)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    categories = Category.objects.all()

    context = {
        'products': products,
        # 'count': Product.objects.count(),
        'categories': categories
    }
    return render(request, 'showProducts.html', context)
# to view the single product details in the productDetails
#@login_required(login_url='accounts/login')
def productDetail(request, pk):
    eachproduct = Product.objects.get(id=pk)
    context = {
        'eachproduct': eachproduct
    }
    return render(request, 'productDetail.html', context)

#  to add the new product from the html template page addProduct.html

@login_required(login_url='showProducts')
def addProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showProducts')
    context = {
        'form': form
    }
    return render(request, 'addProduct.html', context)
#  to update the product form the html template page, updateProduct.html

@login_required(login_url='showProducts')
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)

    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('showProducts')
    context = {
        "form": form
    }
    return render(request, 'updateProduct.html', context)
#  Deleting the record from the table based on the primary key or unique key
@login_required(login_url='showProducts')
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)   #  storing record of 1 or 2 or 3 or 4 in product
    product.delete()  # 1 => deleted

    return redirect('showProducts')
@login_required(login_url='showProducts')
def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            product = Product.objects.filter(description__contains=query)
            return render(request, 'searchbar.html', {"products": product})
        else:
            print("No products Found to show in the Database")
            return render(request, 'searchbar.html', {})
