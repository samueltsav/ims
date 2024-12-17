from django import forms
from .models import Product
from django.contrib.auth.models import User


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        
        labels = {
            'product_id': 'Product ID',
            'name': 'Name',
            'sku': 'SKU',
            'price': 'Price',
            'quantity': 'Quantity',
            'supplier': 'Supplier',
        }

        widgets = {
            'product_id': forms.NumberInput(
                attrs={'placeholder': 'e.g. 1', 'class': 'form-control' }),
            'name': forms.TextInput(
                attrs={'placeholder': 'e.g. shirt', 'class': 'form-control' }),
            'sku': forms.TextInput(
                attrs={'placeholder': 'e.g. S12345', 'class': 'form-control' }),
            'price': forms.NumberInput(
                attrs={'placeholder': 'e.g. 99.99', 'class': 'form-control' }),
            'quantity': forms.NumberInput(
                attrs={'placeholder': 'e.g. 10', 'class': 'form-control' }),
            'supplier': forms.TextInput(
                attrs={'placeholder': 'e.g. OMG Supplies', 'class': 'form-control' }),
        } 
        
        
class RegUserForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
        
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password_confirm']
        
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Passwords don not match!')
        return cleaned_data