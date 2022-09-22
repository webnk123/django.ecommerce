from django.db import models
import datetime




class Product(models.Model):
    product_name = models.CharField(max_length=200)
    old_price = models.CharField(max_length=20, blank=True, null=True)
    price = models.CharField(max_length=20)
    article = models.CharField(max_length=50)
    descrip = models.TextField()
    descripoint = models.TextField(blank=True, null=True)
    images = models.ManyToManyField('ProductImage', related_name='products', blank=True, null=True)
    category = models.ManyToManyField('ProductCategory', related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Products"
        ordering = ['id']

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        name = '/product/' + str(self.pk) + '/'
        return name


class ProductImage(models.Model):
    image = models.ImageField(upload_to='images', blank=True, null=True)



class ProductCategory(models.Model):
    product_category = models.CharField(max_length=20)

    def __str__(self):
        return self.product_category

class Quickorder(models.Model):
    product_name = models.CharField(max_length=200)
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True, null=True)
    comment = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50,blank=True, null=True)
    city = models.CharField(max_length=100, default='Москва',blank=True, null=True)
    address = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=200, blank=True, null=True)


    class Meta:
        ordering = ('-created',)
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return 'Заказ {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity


class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    comment = models.TextField()
    image = models.ImageField(upload_to='images', blank=True, null=True)
    moderated = models.BooleanField(default=False)