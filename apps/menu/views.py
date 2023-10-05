from rest_framework import viewsets, generics
from apps.menu.models import Product, Cart, CartItem
from apps.menu.serializers import ProductSerializer,CartItemSerializer,CartSerializer
# from .serializers import send_order_email

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer