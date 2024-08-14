from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .api import ProductViewSet, CategoryViewSet, SubcategoryViewSet

router = DefaultRouter()

router.register('product', ProductViewSet, 'Product')
router.register('category', CategoryViewSet, 'Category')
router.register('subcategory', SubcategoryViewSet, 'Subcategory')

urlpatterns = [
    path('', include(router.urls)),
]
