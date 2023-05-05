from django.shortcuts import render
from .models import Products, Order

from django.core.paginator import Paginator

# Create your views here.
def index(request):
    product_objects = Products.objects.all()
    
    product_name = request.GET.get('product_name')
    if product_name is not None and product_name != "":
        product_objects = product_objects.filter(title__icontains=product_name)
    
    paginator = Paginator(product_objects, 4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    return render(request, 'shop/index.html', {'product_objects': product_objects})

def detail(request, id):
    
    # quuery the product
    product_object = Products.objects.get(id=id)
    return render(request, 'shop/detail.html', {'product_object': product_object})

def checkout(request):
    
    if request.method == 'POST':
        items = request.POST.get('items', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address','')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        totalPrice = request.POST.get('total', '')
        zipcode = request.POST.get('zipcode', '')
    
    # saving the data gotten from the fields
        
        order = Order(
            items=items,
            name=name, 
            city=city, 
            email=email, 
            state=state, 
            address=address, 
            zipcode=zipcode,
            totalPrice=totalPrice
        )
        order.save()
    
    return render(request, 'shop/checkout.html')