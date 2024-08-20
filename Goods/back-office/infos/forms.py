# forms.py

from django import forms
from Goods.models import Info

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['phone_number', 'email', 'address']
