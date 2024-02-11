import datetime

from django import forms
from .models import Product,Client

class AddNewProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price',  'picture']


