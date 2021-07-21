from .forms import OrderCreateForm
from .models import OrderItem, Quickorder, Review, Product


def save_order(form):
	name = form.cleaned_data['name']
	phone = form.cleaned_data['phone']
	address = form.cleaned_data['address']
	comment = form.cleaned_data['comment']
	city = form.cleaned_data['city']
	email = form.cleaned_data['email']
	order = form.save()
	iden = order.id 

	return email, iden, name, phone, address, comment, city, order


def create_order(cart,order):
	for item in cart:
		OrderItem.objects.create(order=order, 
								product=item['product'],
								price=item['price'],
								quantity=item['quantity'])


def save_quickorder(form):
	obj = Quickorder()
	obj.product_name = form.cleaned_data['product_name']
	phone = obj.phone = form.cleaned_data['phone']
	address = obj.address = form.cleaned_data['address']
	comment = obj.comment = form.cleaned_data['comment']
	this_product = Product.objects.get(id = obj.product_name)
	obj.save()
	iden = obj.id 
	return iden, this_product, phone, address, comment

def create_review(form):
	obj = Review()
	obj.name = form.cleaned_data['name']
	obj.email = form.cleaned_data['email']
	obj.comment = form.cleaned_data['comment']
	obj.image = form.cleaned_data['image']
	obj.save()