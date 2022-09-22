from django import forms
from .models import Order


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class Quickorderform(forms.Form):
    product_name = forms.CharField(max_length=200)
    name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваше имя'}))
    phone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваш телефон'}))
    address = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваш город'}))
    comment = forms.CharField(max_length=200, required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'При желании, вы можете оставить комментарий к заказу','size': '20'}))

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label="Кол-во ")
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name','phone','address','comment','city','email']

class Searchform(forms.Form):
    searched = forms.CharField(max_length=100, label="")

class Reviewform(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваше имя'}))
    email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваш e-mail'}))
    comment = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш отзыв'}))
    image = forms.ImageField(required=False)