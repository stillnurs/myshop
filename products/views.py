from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):  # category_slug is needed to create categories URL
	# if categories don't exist, it has to be None
	category = None
	categories = Category.objects.all()
	products = Product.objects.all()

	if category_slug:  # if slug is not empty and user chooses any of categories
		category = get_object_or_404(Category, slug=category_slug)  # we take category by slug
		products = category.products.filter(category=category)  # we take all products from initial category

	paginator = Paginator(products, 4)
	page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)

	is_paginated = page.has_other_pages()
	if page.has_previous():
		prev_url = '?page={}'.format(page.previous_page_number())
	else:
		prev_url = ''

	if page.has_next():
		next_url = '?page={}'.format(page.next_page_number())
	else:
		next_url = ''

	context = {
		'products': page,
		'is_paginated': is_paginated,
		'next_url': next_url,
		'prev_url': prev_url,
		'category': category,
		'categories': categories,
	}

	return render(request, 'products.html', context)


def product_detail(request, id, slug):
	product = get_object_or_404(Product, slug=slug, id=id, status=True)
	cart_product_form = CartAddProductForm()

	context = {
		'product': product,
		'cart_product_form': cart_product_form,
	}
	return render(request, 'product_detail.html', context)
