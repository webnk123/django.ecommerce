import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pinkoproj.settings")
django.setup()
from sumkiapp.models import Product
import time

def bulk(name, old_price, price, article, descrip, descripoint, primary_image, image2, image3, image4, image5, image6, collection, product_category):
	batch_size = 1
	Product.objects.bulk_create([Product(product_name=name, old_price=old_price, price=price,article=article, descrip=descrip, descripoint=descripoint,primary_image=primary_image, image2=image2, image3=image3,image4=image4, image5=image5, image6=image6, product_collection=collection,product_category=product_category)])

with open('products.txt', 'r') as a:
	for i in a:
		x = i.split(",")
		if "\n" in x[-1]:
			x[-1] = x[-1].strip()
		raw_name = x[0]
		if "/" in raw_name:
			name = raw_name.replace("/", " ")
		else:
			name = raw_name
		del x[0]

		price = x[0]
		del x[0]
		old_price = x[0]
		del x[0]
		article = x[0]
		del x[0]
		raw_image = []
		for i in x:
			if 'images' in i:
				raw_image.append(i)
		if x[-1] == "":
			del x[-1]
		if x[-1] == "":
			del x[-1]
		if x[-1] == "":
			del x[-1]
		if x[-1] == "":
			del x[-1]
		if 'images' in x[-1]:
			del x[-1]
		if 'images' in x[-1]:
			del x[-1]
		if 'images' in x[-1]:
			del x[-1]
		if 'images' in x[-1]:
			del x[-1]
		if 'images' in x[-1]:
			del x[-1]
		if 'images' in x[-1]:
			del x[-1]
		descripoint = x[-1]
		del x[-1]
		final = ''.join(x)
		final = final.replace("]", "")
		final = final.replace("[", "")
		descrip = final
		primary_image = raw_image[0]
		del raw_image[0]
		if len(raw_image) != 0:
			image2 = raw_image[0]
			del raw_image[0]
		else:
			image2 = primary_image
		if len(raw_image) != 0:
			image3 = raw_image[0]
			del raw_image[0]
		else:
			image3 = primary_image
		if len(raw_image) != 0:
			image4 = raw_image[0]
			del raw_image[0]
		else:
			image4 = primary_image
		if len(raw_image) != 0:
			image5 = raw_image[0]
			del raw_image[0]
		else:
			image5 = primary_image
		if len(raw_image) != 0:
			image6 = raw_image[0]
			del raw_image[0]
		else:
			image6 = primary_image
		if 'Ремень' in name:
			product_category = 'Ремень'
			collection = 'Ремень'
		elif 'КОШЕЛЕК' in name:
			product_category = 'КОШЕЛЕК'
			collection = 'КОШЕЛЕК'
		else:
			product_category = 'Bag'
		if 'Puff' in name:
			collection = 'Puff Love Bag'
		else:
			collection = 'Big Love Bag'
		bulk(name, old_price, price, article, descrip, descripoint, primary_image, image2, image3, image4, image5, image6, collection, product_category)

