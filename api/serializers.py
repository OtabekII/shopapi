from rest_framework.serializers import ModelSerializer
from Goods.models import Banner, Product, Category, Cart, Order, WishList, ProductEnter, Info, CartProduct
from rest_framework import serializers

class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
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


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class ProductEnterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductEnter
        fields = '__all__'


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = '__all__'


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'



class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = '__all__'
