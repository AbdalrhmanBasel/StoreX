"""
1. User Form.
2. Order Instance.
3. Clear cart's content -> redirect to success page.
"""
from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
