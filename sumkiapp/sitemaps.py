from django.contrib import sitemaps
from .models import Product
from django.urls import reverse
from django.contrib.sitemaps import Sitemap


class ProductSitemap(sitemaps.Sitemap):
	changefreq = "weekly"
	priority = 1.0

	def items(self):	
		return Product.objects.all()

	def lastmod(self, obj):
		return obj.created_at


class StaticViewSitemap(sitemaps.Sitemap):
	priority = 0.9
	changefreq = 'weekly'

	def items(self):
		return ['homepage', 'contacts', 'reviews', 'about', 'delivery', 'privacy_policy', 'terms_of_use','auth']

	def location(self, item):
		return reverse('sumkiapp:' + str(item))


class CollectionSitemap(Sitemap):
	changefreq = "never"
	priority = 0.8

	def items(self):
		return ['Lorem','ipsum', 'dolor','sit']

	def location(self, item):
		return '/' + str(item)