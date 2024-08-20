from rest_framework.serializers import ModelSerializer
from Goods.models import Banner, Product, Category, Cart
from rest_framework import serializers

class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'
        
        
class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        
        
        
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
        
        
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'