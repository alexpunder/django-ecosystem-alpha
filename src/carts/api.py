from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from .models import Cart
from .services import CartService
from .serializers import CartSerializer, CartItemSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    @action(
        detail=False, methods=['get'],
        permission_classes=[IsAuthenticated],
    )
    def get_user_cart(self, request, **kwargs):
        print(request.user)
        user_cart = CartService.get_user_cart(user=self.request.user)
        products = user_cart.get_cart_items()
        print(f'{products=}')
        serializer = CartItemSerializer(
            data=products, context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
