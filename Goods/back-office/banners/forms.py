from django import forms
from Goods.models import Banner

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['title', 'sub_title', 'img', 'is_active']
