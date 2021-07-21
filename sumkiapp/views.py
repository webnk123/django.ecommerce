from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_GET
from .cart import *
from .models import Product, Quickorder, Review
from .forms import Quickorderform, CartAddProductForm, OrderCreateForm, Searchform, Reviewform
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse
from django.conf import settings
from django.contrib.staticfiles import finders
from .obj_create import save_order, create_order, save_quickorder, create_review
from .email_logic import moscowtime, logo_data, mail_validation, send_quickorder_email, send_order_email


def auth(request):
	return render(request, 'sumkiapp/auth.html')

def product_view(request, ide):
	this_product = Product.objects.get(id = ide)
	form = Quickorderform(initial={'product_name': this_product.id})
	form2 = CartAddProductForm()
	return render(request, 'sumkiapp/product_page.html', {"product": this_product, 'form':form, 'form2':form2})

def order_create(request):
	cart = Cart(request)
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order_create_and_send(form,cart)
			cart.clear()
			return render(request, 'sumkiapp/created.html', {'order': order})
	else:
		form = OrderCreateForm
	return render(request, 'sumkiapp/create.html', {'cart': cart, 'form': form})

def is_ajax(request):
	return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"

@require_GET
def homepage(request):
	products_all = Product.objects.all()
	paginator = Paginator(products_all, per_page=12)
	page_num = int(request.GET.get("page", 1))
	if page_num > paginator.num_pages:
		return HttpResponse(status=200)
	products = paginator.page(page_num)
	context = {'products': products}
	if is_ajax(request):
		return render(request, 'sumkiapp/_products.html', {'products': products})
	return render(request, 'sumkiapp/homepage.html', context)

def delivery(request):
	return render(request, 'sumkiapp/delivery.html')

def backpacks(request):
	backpacks = Product.objects.filter(product_category__contains= "Backpack")
	return render(request, 'sumkiapp/backpacks.html', context = {"products": backpacks})

def about(request):
	return render(request, 'sumkiapp/about.html')

def reviews(request):
	mod_reviews = Review.objects.filter(moderated=True)
	form = Reviewform()
	return render(request, 'sumkiapp/reviews.html', {'form':form, 'reviews': mod_reviews})

def contacts(request):
	return render(request, 'sumkiapp/contacts.html')

def collection(request, coll_name):
	collections = ['Puff-Love-Bag','Big-Love-Bag', 'Mini-Love-Bag','Round-Love-Bag','wallet','belts']
	if coll_name in collections:
		coll_name2 = coll_name.replace('-', ' ')
		content = Product.objects.filter(product_collection__contains=coll_name2)
		return render(request, 'sumkiapp/collection.html', {"products": content, "coll": coll_name})
    
	return render(request, "sumkiapp/404page.html", status=404) 

def new_quickorder(request):
	if request.method == 'POST':
		form = Quickorderform(request.POST)
		if form.is_valid():
			quickorder_create_and_send(form)
			return redirect('/')

@require_POST
def cart_add(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)
	form = CartAddProductForm(request.POST)
	if form.is_valid():
		cd = form.cleaned_data
		cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
	return redirect('sumkiapp:cart_detail')

def cart_remove(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)
	cart.remove(product)
	return redirect('sumkiapp:cart_detail')

def cart_detail(request):
	cart = Cart(request)
	return render(request, 'sumkiapp/detail.html', {'cart': cart})

def terms_of_use(request):
	return render(request, 'sumkiapp/terms_of_use.html')

def privacy_policy(request):
	return render(request, 'sumkiapp/privacy_policy.html')

def error_404(request, exception):
	return render(request, "sumkiapp/404page.html", status=404)


def error_500(request):
	return render(request, 'sumkiapp/500page.html', status=500)

@require_POST
def search(request):
	form = Searchform(request.POST)
	if form.is_valid():
		searchword = form.cleaned_data['searched']
		content = Product.objects.filter(product_name__contains=searchword)
		return render(request, 'sumkiapp/searched.html', {"products": content, "searchword": searchword})


def add_to_fav(request, id):
	if request.method == 'POST':
		if not request.session.get('favorites'):
			request.session['favorites'] = list()
		else:
			request.session['favorites'] = list(request.session['favorites'])

		item_exists = next((item for item in request.session['favorites'] if item['type'] == request.POST.get('type') and item['id'] == id), False)

		add_data = {
			'type': request.POST.get('type'),
			'id': id,
		}

		if not item_exists:
			request.session['favorites'].append(add_data)
			request.session.modified = True
	return redirect(request.POST.get('url_from'))


def remove_from_fav(request, id):
	if request.method == 'POST':

		for item in request.session['favorites']:
			if item['id'] == id and item['type'] == request.POST.get('type'):
				item.clear()

		while {} in request.session['favorites']:
			request.session['favorites'].remove({})

		if not request.session['favorites']:
			del request.session['favorites']

		request.session.modified = True
	return redirect(request.POST.get('url_from'))

def favorites(request):
	favs = []
	if not request.session.get('favorites'):
		request.session['favorites'] = list()

		fav_products = []

	else:
		for item in request.session['favorites']:
			favs.append(item['id'])
			fav_products = Product.objects.filter(pk__in=favs)
	
	return render(request, 'sumkiapp/favs.html', {"products": fav_products})







def catalog(request):
	products = Product.objects.all().order_by('id')[:8]
	return render(request, 'sumkiapp/catalog.html', {"products": products})

def review_add(request):
	if request.method == 'POST':
		form = Reviewform(request.POST, request.FILES)
		if form.is_valid():
			create_review(form)
			return redirect('/')