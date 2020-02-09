from django import forms
from .models import Product
class addProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title","content","isPrivate","productImage",'productPrice']

