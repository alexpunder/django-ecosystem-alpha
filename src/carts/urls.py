from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .api import CartViewSet

router = DefaultRouter()

router.register('cart', CartViewSet, 'Cart')

urlpatterns = [
    path('', include(router.urls)),
]
