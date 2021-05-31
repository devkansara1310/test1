from django import forms
from .models import Customer,Order, Product

class orderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        

class updateorderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        
    