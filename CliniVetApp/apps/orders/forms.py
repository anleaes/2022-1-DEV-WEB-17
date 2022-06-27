from django import forms
from .models import Order, Client, OrderItem ,Services

class OrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        exclude = ('client', 'created_on' , 'updated_on')

class OrderItemForm(forms.ModelForm):
    
    class Meta:
        model = OrderItem
        exclude = ('order', 'created_on' , 'updated_on')
