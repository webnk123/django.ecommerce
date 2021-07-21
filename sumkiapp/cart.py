from decimal import Decimal
from django.conf import settings
from .models import Product


class Cart(object):

	def __init__(self, request):
		#init cart
		self.session = request.session
		cart = self.session.get(settings.CART_SESSION_ID)
		if not cart:
			# save empty cart in session if not cart
			cart = self.session[settings.CART_SESSION_ID] = {}
		self.cart = cart

	def add(self, product, quantity=1, update_quantity=False):
		# add product to cart or update quantity
		product_id = str(product.id)
		if product_id not in self.cart:
			self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}

		if update_quantity:
			self.cart[product_id]['quantity'] = quantity
		else:
			self.cart[product_id]['quantity'] += quantity

		self.save()

	def save(self):
		# update cart session
		self.session[settings.CART_SESSION_ID] = self.cart
		# mark as changed
		self.session.modified = True

	def remove(self, product):
		#delete product from cart
		product_id = str(product.id)
		if product_id in self.cart:
			del self.cart[product_id]
			self.save()

	def __iter__(self):
		# iterate over cart items, get products from db
		product_ids = self.cart.keys()
		products = Product.objects.filter(id__in = product_ids)
		for product in products:
			self.cart[str(product.id)]['product'] = product

		for item in self.cart.values():
			item['price'] = Decimal(str(item['price']).replace(",",''))
			item['total_price'] = item['price'] * item['quantity']
			yield item

	def __len__(self):
		# count amount of products in cart
		return sum(item['quantity'] for item in self.cart.values())

	def get_total_price(self):
		# count total price of cart
		return sum(Decimal(item['price'] * item['quantity']) for item in self.cart.values())

	def clear(self):
		# delete cart form session
		del self.session[settings.CART_SESSION_ID]
		self.session.modified =True