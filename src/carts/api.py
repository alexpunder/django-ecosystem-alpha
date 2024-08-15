from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from .services import CartService
from .serializers import CartSerializer


class CartViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @action(
        detail=False, methods=['get'],
    )
    def get_user_cart(self, request):
        user_cart = CartService.get_user_cart(request.user)
        serializer = CartSerializer(
            user_cart, context={'request': request},
        )
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        detail=False, methods=['post'],
        url_path=r'add_to_user_cart/(?P<product_id>\d+)',
    )
    def add_to_user_cart(self, request, product_id=None):
        quantity = request.data.get('quantity', 1)
        CartService.add_to_user_cart(
            user=request.user,
            product_id=product_id,
            quantity=quantity,
        )
        return Response(status=status.HTTP_200_OK)

    @action(
        detail=False, methods=['post'],
        url_path=r'delete_item_from_user_cart/(?P<product_id>\d+)',
    )
    def delete_item_from_user_cart(self, request, product_id=None):
        CartService.delete_user_cart_item(
            user=request.user,
            product_id=product_id,
        )
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(
        detail=False, methods=['post'],
    )
    def clear_user_cart(self, request):
        user_cart = CartService.get_user_cart(request.user)
        user_cart.clear_cart()
        return Response(status=status.HTTP_204_NO_CONTENT)
