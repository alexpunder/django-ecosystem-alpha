## Описание проекта.

_**Экосистема-Альфа**_ - тестовое задание на Django Rest Framework (DRF), реализущее проект простого магазина продуктов со следующим функционалом:
1. Работа с категориями, подкатегориями и товарами через админ-панель и соответствующие с ними действия: добавления, изменения, удаления;
2. Работа с корзиной пользователя: добавление товара, его удаление, очистка корзины и просмотр ей текущего содержания. Получение общей стоимости как самих товаров, так и общей стоимости самой корзины;
3. Аутентификация пользователя по JWT-токену;
4. Простая пагинация отдаваемых данных;
5. Эндпоинты категорий, подкатегорий и товаров доступны всем пользователям (только безопасные матоды), эндпоинты корзины - зарегистрированному пользователю.

## Используемые технологии.

Django REST Framework (DRF), Django-filter, Djangorestframework-simplejwt, Djoser

## Установка проекта.

1. Находясь в дериктории, где будет размещаться проект, склонируйте его репозиторий:  
```
git@github.com:alexpunder/django-ecosystem-alpha.git
```
2. Перейди в папку проекта:  
```
cd django-ecosystem-alpha
```
3. Создайте виртуальное окружение и активируйте его (команды для Windows):
```
python -m venv venv
```
```
source  venv/Scripts/activate
```
4. Создайте и заполните .env-файл необходимыми данными  
5. Для корректной работы приложения, выполните следующие команды:
```
python src/manage.py makemigrations
```
```
python src/manage.py makemigrations
```
6. Для запуска локального сервера, используя терминал, введите команду:  
```
python src/manage.py runserver
```
## Примеры запросов.

1. Получение публикации
 - в GET-запросе по адресу `...api/product/{product_id}/` любым пользователем, передать **id** товара. Ответ будет следующего вида:
```
{
    "name": "test",
    "slug": "test",
    "price": "250.00",
    "category": {
        "name": "test cat",
        "slug": "test-cat",
        "image": "http://127.0.0.1:8000/some-path/test_cat.jpg"
    },
    "subcategory": {
        "name": "test subacat",
        "slug": "test-subacat",
        "image": "http://127.0.0.1:8000/some-path/test_subcat.jpg"
    },
    "images": [
        {
            "image": "http://127.0.0.1:8000/some-path/test_1.jpg",
            "size": "SMALL"
        },
        {
            "image": "http://127.0.0.1:8000/some-path/test_2.jpg",
            "size": "MEDIUM"
        },
        {
            "image": "http://127.0.0.1:8000/some-path/test_3.jpg",
            "size": "LARGE"
        }
    ]
}
```
2. Запрос на получение корзины пользователя (доступен только авторизованным)
 - GET-запрос доступен по адресу `...api/cart/get_user_cart/`
```
{
    "user": {
        "username": "alex123"
    },
    "products": [
        {
            "product": {
                "name": "test",
                "slug": "test",
                "price": "250.00",
                "category": {
                    "name": "test cat",
                    "slug": "test-cat",
                    "image": "http://127.0.0.1:8000/some-path/test_cat.jpg"
                },
                "subcategory": {
                    "name": "test subacat",
                    "slug": "test-subacat",
                    "image": "http://127.0.0.1:8000/some-path/test_subcat.jpg"
                },
                "images": [
                    {
                        "image": "http://127.0.0.1:8000/some-path/test_1.jpg",
                        "size": "SMALL"
                    },
                    {
                        "image": "http://127.0.0.1:8000/some-path/test_2.jpg",
                        "size": "MEDIUM"
                    },
                    {
                        "image": "http://127.0.0.1:8000/some-path/test_3.jpg",
                        "size": "LARGE"
                    }
                ]
            },
            "quantity": 2,
            "item_total_price": 500.0
        },
        {
            "product": {
                "name": "test-2",
                "slug": "test-2",
                "price": "300.00",
                "category": {
                    "name": "test cat",
                    "slug": "test-cat",
                    "image": "http://127.0.0.1:8000/some-path/test_cat.jpg"
                },
                "subcategory": {
                    "name": "test subacat",
                    "slug": "test-subacat",
                    "image": "http://127.0.0.1:8000/some-path/test_subcat.jpg"
                },
                "images": []
            },
            "quantity": 1,
            "item_total_price": 300.0
        }
    ],
    "cart_items_total_price": 800.0,
    "cart_items_count": 2
}
```
