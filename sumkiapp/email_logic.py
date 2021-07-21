from datetime import datetime
from time import gmtime, strftime
from django.conf import settings
from .models import Product
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from email.mime.image import MIMEImage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .obj_create import save_order, create_order, save_quickorder
import pytz


# function used to get current Moscow time to attach to email
def moscowtime():
	MSK = pytz.timezone('Europe/Moscow')
	datetime_msk = datetime.now(MSK)
	return datetime_msk.strftime("%d-%m-%y %H:%M")

#function used to attach images to email via cid
def logo_data(img_path, pk):
    with open(img_path, 'rb') as f:
        logo_data = f.read()
    logo = MIMEImage(logo_data, 'jpeg')
    cidname = '<' + str(pk) + '>'
    logo.add_header('Content-ID', cidname)
    return logo

# used to validate email passed in a form and create a recipient list.
# If "email" is valid rec_list consists of host email and client email
# if "email" isn't valid message gets sent only to host as a notification of new order
def mail_validation(email):
	try:
		validate_email(email)
		rec_list = [settings.EMAIL_HOST_USER, email]
	except validate_email.ValidationError:
		rec_list = [settings.EMAIL_HOST_USER]
	return rec_list

def send_quickorder_email(iden, this_product, showtime, phone, address, comment):
	rec_list = [settings.EMAIL_HOST_USER]
	topic = "Быстрый Заказ №:"  + str(iden)
	html_content = render_to_string("sumkiapp/quick_email_template.html", {'iden': iden, 'product': this_product, 'time': showtime, 'phone': phone, 'address': address, 'comment': comment})
	text_content = strip_tags(html_content)

	email = form_email_multialt(topic, text_content, rec_list, html_content)

	img_path = settings.BASE_DIR + this_product.primary_image.url
	pk = this_product.pk
	email.attach(logo_data(img_path, pk))
	email.send(fail_silently=False)

def send_order_email(showtime, name, phone, address, comment, city, email, cart, iden, rec_list):
	topic = "Номер Заказа:  " + str(iden)
	html_content = render_to_string("sumkiapp/order_email_template.html", {'time': showtime, 'name': name, 'phone': phone, 'address': address, 'comment': comment, 'city': city, 'email': email, 'cart': cart, 'iden': iden})
	text_content = strip_tags(html_content)

	email = form_email_multialt(topic, text_content, rec_list, html_content)

	for item in cart:
		this_product = Product.objects.get(product_name = item['product'])
		img_path = settings.BASE_DIR + this_product.primary_image.url
		pk = this_product.pk
		email.attach(logo_data(img_path, pk))

	email.send(fail_silently=False)

def form_email_multialt(topic, text_content, rec_list, html_content):
	email = EmailMultiAlternatives(
		#subject
		topic,
		#content
		text_content,
		#from email
		settings.EMAIL_HOST_USER,
		#rec list
		rec_list)
	email.mixed_subtype = 'related'
	email.attach_alternative(html_content, "text/html")

	return email


def order_create_and_send(form,cart):
	email, iden, name, phone, address, comment, city, order = save_order(form)
	rec_list = mail_validation(email)
	create_order(cart,order)
	showtime = moscowtime()
	send_order_email(showtime, name, phone, address, comment, city, email, cart, iden, rec_list)

def quickorder_create_and_send(form):
	iden, this_product, phone, address, comment = save_quickorder(form)
	showtime = moscowtime()
	send_quickorder_email(iden, this_product, showtime, phone, address, comment)