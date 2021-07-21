from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import ProductSitemap, StaticViewSitemap, CollectionSitemap


app_name = "sumkiapp"

sitemaps = {
	'products': ProductSitemap,
	'static': StaticViewSitemap,
	'collect': CollectionSitemap,
} 

urlpatterns = [
	path('auth/', views.auth, name='auth'),
	path('review_add', views.review_add, name='review_add'),
	path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
	path('robots.txt', TemplateView.as_view(template_name='sumkiapp/robots.txt', content_type='text/plain')),
	path('', views.homepage, name='homepage'),
	path('catalog/', views.homepage, name='homepage'),
	path('favorites/', views.favorites, name='favorites'),
	path('addfav/<id>', views.add_to_fav, name='add_to_fav'),
	path('removefav/<id>', views.remove_from_fav, name='remove_from_fav'),
	path('product/<ide>/', views.product_view, name='product_view'),
	path('search/', views.search, name='search'),
	path('terms-of-use/', views.terms_of_use, name="terms_of_use"),
	path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
	path('create/', views.order_create, name='order_create'),
	path('products/', views.homepage, name='homepage'),
	path('cart/', views.cart_detail, name='cart_detail'),
	path('add/<product_id>/', views.cart_add, name='cart_add'),
	path('remove/<product_id>/', views.cart_remove, name='cart_remove'),
	path('delivery/', views.delivery, name='delivery'),
	path('Backpacks/', views.backpacks, name='backpacks'),
	path('about/', views.about, name='about'),
	path('reviews/', views.reviews, name='reviews'),
	path('contacts/', views.contacts, name='contacts'),
	path('fast_order/', views.new_quickorder, name='fast_order'),
	path("<coll_name>/", views.collection, name='collection'),


	]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

