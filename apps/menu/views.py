from rest_framework import viewsets
from apps.menu.models import Product, Cart
from apps.menu.serializers import ProductSerializer,CartSerializer
# from .serializers import send_order_email

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer