from rest_framework.decorators import api_view 
from rest_framework.response import Response
 
 
from .serializers import BannerSerializer, ProductSerializer, CategorySerializer, ContactSerializer
from Goods.models import Banner, Contact, Product, Category, Cart
from .serializers import CartSerializer
 
 
 
@api_view(['GET']) 
def banner_list(request): 
    banners = Banner.objects.all() 
    serializer_data = BannerSerializer(banners, many=True)  
    return Response(serializer_data.data) 

@api_view(['GET']) 
def banner_create(request):
    serializer = BannerSerializer(data=request.data) 
    if serializer.is_valid(): 
        serializer.save() 
        return Response(serializer.data) 
    return Response(serializer.errors)
 

@api_view(['GET'])
def banner_update(request, id):
    banner = Banner.objects.get(id=id) 
    serializer = BannerSerializer(banner, data=request.data) 
    if serializer.is_valid(): 
        serializer.save() 
        return Response(serializer.data) 
    return Response(serializer.errors)


@api_view(['GET']) 
def banner_detail(request, id): 
    banner = Banner.objects.get(id=id) 
    ser_data = BannerSerializer(banner).data 
    return Response(ser_data) 

@api_view(['GET'])
def banner_delete(request, id):
    banner = Banner.objects.get(id=id) 
    banner.delete() 
    return Response(status=204)  # No Content

 
@api_view(['GET']) 
def contact_list(request): 
    contants = Contact.objects.all() 
    serializer_data = ContactSerializer(contants, many=True)  
    return Response(serializer_data.data) 

@api_view(['GET']) 
def contact_create(request):
    serializer = ContactSerializer(data=request.data) 
    if serializer.is_valid(): 
        serializer.save() 
        return Response(serializer.data) 
    return Response(serializer.errors)

@api_view(['GET']) 
def contact_detail(request, id): 
    contact = Contact.objects.get(id=id) 
    con_data = ContactSerializer(contact).data 
    return Response(con_data) 

@api_view(['GET']) 
def contact_update(request, id):
    contact = Contact.objects.get(id=id) 
    serializer = ContactSerializer(contact, data=request.data) 
    if serializer.is_valid(): 
        serializer.save() 
        return Response(serializer.data) 
    return Response(serializer.errors)

@api_view(['GET']) 
def contact_delete(request, id):
    contact = Contact.objects.get(id=id) 
    contact.delete() 
    return Response(status=204)  
 
 
 
 
@api_view(['GET']) 
def product_list(request): 
    products = Product.objects.all() 
    serializer_data = ProductSerializer(products, many=True)  
    return Response(serializer_data.data) 

@api_view(['GET']) 
def product_create(request):
    serializer = ProductSerializer(data=request.data) 
    if serializer.is_valid(): 
        serializer.save() 
        return Response(serializer.data) 
    return Response(serializer.errors)

@api_view(['GET']) 
def product_update(request, id):
    product = Product.objects.get(id=id) 
    serializer = ProductSerializer(product, data=request.data) 
    if serializer.is_valid(): 
        serializer.save() 
        return Response(serializer.data) 
    return Response(serializer.errors)
 
@api_view(['GET']) 
def product_detail(request, id): 
    product = Product.objects.get(id=id) 
    pro_data = ProductSerializer(product).data 
    return Response(pro_data) 

@api_view(['GET']) 
def product_delete(request, id):
    product = Product.objects.get(id=id) 
    product.delete() 
    return Response(status=204)  
 
 
 
@api_view(['GET']) 
def category_list(request): 
    categorys = Category.objects.all() 
    serializer_data = CategorySerializer(categorys, many=True)  
    return Response(serializer_data.data) 

@api_view(['GET']) 
def category_create(request):
    serializer = CategorySerializer(data=request.data) 
    if serializer.is_valid(): 
        serializer.save() 
        return Response(serializer.data) 
    return Response(serializer.errors)

@api_view(['GET']) 
def category_update(request, id):
    category = Category.objects.get(id=id) 
    serializer = CategorySerializer(category, data=request.data) 
    if serializer.is_valid(): 
        serializer.save() 
        return Response(serializer.data) 
    return Response(serializer.errors)
 
@api_view(['GET']) 
def category_detail(request, id): 
    category = Category.objects.get(id=id) 
    cat_data = CategorySerializer(category).data 
    return Response(cat_data)

@api_view(['GET']) 
def category_delete(request, id):
    category = Category.objects.get(id=id) 
    category.delete() 
    return Response(status=204)

@api_view(['GET'])
def last_achive_cart(request):
    last_archived_cart = Cart.objects.filter(is_archived=True).last()
    serializer = CartSerializer(last_archived_cart) if last_archived_cart else None
    return Response(serializer.data if serializer else {"detail": "No archived cart found"}, status=200)

@api_view(['POST'])
def add_product(request):
    product_id = request.data.get('product_id')
    cart_id = request.data.get('cart_id')

    cart = Cart.objects.get(id=cart_id)  # Assume the cart exists
    product = Product.objects.get(id=product_id)  # Assume the product exists
    cart.items.add(product)
    cart.save()
    return Response({"detail": "Product added to cart"}, status=200)

@api_view(['POST'])
def remove_product(request):
    product_id = request.data.get('product_id')
    cart_id = request.data.get('cart_id')

    cart = Cart.objects.get(id=cart_id)  # Assume the cart exists
    product = Product.objects.get(id=product_id)  # Assume the product exists
    cart.items.remove(product)
    cart.save()
    return Response({"detail": "Product removed from cart"}, status=200)

@api_view(['GET'])
def product_enter(request, product):
    cart_id = request.GET.get('cart_id')
    cart = Cart.objects.get(id=cart_id)  # Assume the cart exists
    product = Product.objects.get(id=product)  # Assume the product exists
    cart.items.add(product)
    cart.save()
    return Response({"detail": "Product added to cart"}, status=200)

@api_view(['GET'])
def wishlist(request, ) :
    user = request.user
    wishlist = user.wish_list
    serializer = ProductSerializer(wishlist, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def info_list(request, ) :
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
def info_crate(request, ) :
    serializer = ContactSerializer(Contact.objects.all(), many=True)
    return Response(serializer.data)

@api_view(['GET'])
def info_detail(request, id) :
    contact = Contact.objects.get(id=id)
    serializer = ContactSerializer(contact)
    return Response(serializer.data)

@api_view(['GET'])
def info_update(request, id) :
    contact = Contact.objects.get(id=id)
    serializer = ContactSerializer(contact, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
def info_delete(request, id) :
    contact = Contact.objects.get(id=id)
    contact.delete()
    return Response(status=204)

@api_view(['GET'])
def cart_products(request, id):
    cart = Cart.objects.get(id=id)
    serializer = ProductSerializer(cart.items.all(), many=True)
    return Response(serializer.data)
