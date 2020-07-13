from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Category, Product

# Create your views here.
# def home_page(request):

# 	context = {}
# 	return render(request, 'home/home.html', context)

def products_by_category(request, category_id=None, category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	if category_slug:
		category = get_object_or_404(Furniture, slug=category_slug, id=category_id)
		products = products.filter(category=category)

	context = {
		'single_category': category,
		'all_categories': categories,
		'all_products': products
	}
	return render(request, 'home/home.html', context)
	
# https://stackoverflow.com/questions/58145819/count-all-products-in-all-subcategories-recursively