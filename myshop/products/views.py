from django.shortcuts import render
from django.db.models import Avg, Count
from .models import Product, Category

# Create your views here.
def index(request):
    categories = Category.objects.all().annotate(product_count=Count("product")).prefetch_related("product_set")# Fetch all categories
    products = Product.objects.all().order_by("-price").select_related("category")  # Order high to low
    
    # Calculate the average price
    price_avg = products.aggregate(Avg("price"))["price__avg"]

    context = {
        "categories": categories,
        "products": products,
        "price_avg": price_avg,
       
    }

    return render(request, "index.html", context)
