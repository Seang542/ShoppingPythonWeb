from django.shortcuts import render
from productsapp.models import Product
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    products = Product.objects.filter(isTrending=True)
    return render(request,'index.html',{'products':products})

def productDetail(request,id):
    product = Product.objects.get(pk=id)
    return render(request,'detail.html',{'product':product})

def products(request):
    All_products = Product.objects.all()
    #ກຳນົດໝາຍເລກໜ້າ
    page = request.GET.get('page')
    paginator = Paginator(All_products,6)
    All_products = paginator.get_page(page)
    return render(request,'products.html',{'All_products':All_products})