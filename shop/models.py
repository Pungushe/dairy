from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = (
    ('CR', 'Творог'),
    ('ML', 'Молоко'),
    ('LS', 'Ласси'),
    ('MS', 'Коктейль'),
    ('PN', 'Панир'),
    ('GH', 'Топленое масло'),
    ('CZ', 'Сыр'),
    ('IC', 'Мороженое'),
)


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    selling_price = models.FloatField(verbose_name="Цена")
    discount_price = models.FloatField(verbose_name="Скидка")
    description = models.TextField(verbose_name="Описание")
    composition = models.TextField(default='', verbose_name="Состав")
    prodapp = models.TextField(default='', verbose_name="Продукт")
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2, verbose_name="Категории")
    product_image = models.ImageField(upload_to='product', verbose_name="Изображение")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name="Имя")
    locality = models.CharField(max_length=200, verbose_name="Место")
    city = models.CharField(max_length=50, verbose_name="Город")
    mobile = models.IntegerField(default=0, verbose_name="Мобильный телефон")
    zipcode = models.IntegerField(verbose_name="Индекс")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discount_price

    class Meta:
        verbose_name = verbose_name_plural = "Корзина"


STATUS_CHOISES = (
    ('Accepted', 'Принимается'),
    ('Packed', 'Подготовлен к отправке'),
    ('On the Way', 'В пути'),
    ('Delivered', 'Доставлен'),
    ('Cancel', 'Отменен'),
    ('В ожидании', 'В ожидании'),
)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    amount = models.FloatField(verbose_name="Количество")
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True, verbose_name="Заказ")
    razorpay_order_status = models.CharField(max_length=100, blank=True, null=True, verbose_name="Заказ по статусу")
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True, verbose_name="Оплата")
    paid = models.BooleanField(default=False, verbose_name="Оплачено")

    class Meta:
        verbose_name = verbose_name_plural = "Оплата"


class OrderPlace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Покупатель")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    order_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата заказа")
    status = models.CharField(max_length=50, choices=STATUS_CHOISES, verbose_name="Статус", default="В ожидании")
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, default="", verbose_name="Оплата")

    @property
    def total_cost(self):
        return self.quantity * self.product.discount_price

    class Meta:
        verbose_name = "Место заказа"
        verbose_name_plural = "Место заказов"


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")

