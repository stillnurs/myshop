from decimal import Decimal
from django.conf import settings
from products.models import Product


class Cart(object):
	def __init__(self, request):

		self.session = request.session  # requests previous/existing sessions
		cart = self.session.get(settings.CART_SESSION_ID)

		if not cart:  # if session is empty, function initiates new session "cart"
			cart = self.session[settings.CART_SESSION_ID] = {}
		self.cart = cart

	def add(self, product, quantity=1, update_quantity=False):
		"""Adding product to cart or updates it quantities"""
		product_id = str(product.id)

		if product_id not in self.cart:
			self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
		if update_quantity:
			self.cart[product_id]['quantity'] = quantity
		else:
			self.cart[product_id]['quantity'] += quantity
		self.save()

	def save(self):  # Mark the session as edited
		self.session.modified = True

	def remove(self, product):
		""" Removing product from cart"""
		product_id = str(product.id)
		if product_id in self.cart:
			del self.cart[product_id]
		self.save()

	def __iter__(self):
		"""Iterate through products and get corresponding Product objects"""
		product_ids = self.cart.keys()

		# We get Product objects and transfer them into the cart.
		products = Product.objects.filter(id__in=product_ids)
		cart = self.cart.copy()
		for product in products:
			cart[str(product.id)]['product'] = product
		for item in cart.values():
			item['price'] = Decimal(item['price'])
			item['total_price'] = item['price'] * item['quantity']
		yield item

	def __len__(self):
		"""Returns total quantity of products in cart"""
		return sum(item['quantity'] for item in self.cart.values())

	def get_total_price(self):
		return sum(
			Decimal(item['price']) * item['quantity']
			for item in self.cart.values()
		)

	def clear(self):
		del self.session[settings.CART_SESSION_ID]
		self.save()
