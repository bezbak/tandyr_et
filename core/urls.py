from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static
from rest_framework import routers
from apps.menu.views import ProductViewSet, CartViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'cart', CartViewSet)

api_urlpatterns = [
    path('menu/', include('apps.menu.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns)),
    path('api/', include(router.urls)),
    path('',RedirectView.as_view(url='/api/')),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)