from rest_framework import viewsets, generics
from apps.menu.models import Product, Cart, Category
from apps.menu.serializers import ProductSerializer,CartSerializer,CategorySerializer
# from .serializers import send_order_email

# Create your views here.
class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer