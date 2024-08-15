from rest_framework import status
from rest_framework.exceptions import ValidationError


def check_correct_qty(cart_item, quantity, created=False):
    if not created:
        check_qty = cart_item.quantity + quantity
        if check_qty < 1:
            raise ValidationError(
                detail=(
                    'Значение товара в корзине не может быть меньше единицы.'
                ),
                code=status.HTTP_400_BAD_REQUEST,
            )
        return check_qty

    elif quantity < 1:
        raise ValidationError(
            detail=(
                'Значение товара в корзине не может быть меньше единицы. '
                'Добавлен одна единица товара.'
            ),
            code=status.HTTP_400_BAD_REQUEST,
        )

    return quantity
