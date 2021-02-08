from django import forms
from django.forms import widgets
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class OrderForm(forms.ModelForm):

    class Meta:
        model = Orders
        fields = '__all__'
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control', 'id': 'name'}),
            'product': forms.Select(attrs={'class': 'form-control', 'id': 'product'}),
            'status': forms.Select(attrs={'class': 'form-control', 'id': 'status'})
        }


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'type': 'text'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'id': 'phone', 'type': 'phone'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'id': 'email', 'type': 'email'})
        }


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'type': 'text'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'id': 'price', 'type': 'number'}),
            'category': forms.Select(attrs={'class': 'form-control', 'id': 'category'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control', 'id': 'tags'}),
        }


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'username', 'type': 'text'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'id': 'email', 'type': 'email'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
