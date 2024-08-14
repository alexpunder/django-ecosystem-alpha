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
    permission_classes = [IsAuthenticated]

    @action(
        detail=False, methods=['get'],
        permission_classes=[IsAuthenticated],
    )
    def get_user_cart(self, request, **kwargs):
        user_cart = CartService.get_user_cart(request.user)
        products = user_cart.get_cart_items()
        serializer = CartItemSerializer(
            products, many=True, context={'request': request},
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
