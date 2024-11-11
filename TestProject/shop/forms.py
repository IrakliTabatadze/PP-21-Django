from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ('name', 'price', 'stock')
        widgets = {
            'category': forms.CheckboxSelectMultiple(attrs={'class': 'form-control d-flex'}),
            'name': forms.TextInput(attrs={'placeholder': 'Please input name of product'}),
            'description': forms.Textarea(attrs={'placeholder': 'Please input the description of product'})
        }