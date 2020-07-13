from django.shortcuts import render, get_object_or_404

from .models import Category, Product

# Create your views here.
def products_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)

	context = {
		'single_category': category,
		'all_categories': categories,
		'all_products': products
	}
	return render(request, 'home/home.html', context)

# https://stackoverflow.com/questions/58145819/count-all-products-in-all-subcategories-recursively

def product_detail(request, id, slug):
	product = get_object_or_404(Product, id=id, slug=slug, available=True)

	context = {'product': product}
	return render(request, 'home/detail.html', context)