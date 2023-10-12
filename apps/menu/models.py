from django.db import models
from slugify import slugify

class Category(models.Model):
    name = models.CharField(
        max_length=55,
        verbose_name='Название категории'
    )
    slug = models.SlugField(
        unique=True,
        auto_created=True,
        blank=True,
        null=True
    )
    def save(self, *args, **kwargs):
        if self.slug:
            self.slug = self.slug
        else:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)  

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    name = models.CharField(verbose_name='Название блюдо',max_length=1555)
    price = models.DecimalField(verbose_name='Цена',max_digits=10, decimal_places=2)
    image = models.FileField(upload_to='menu_images/')
    
    def __str__(self):
        return f"{self.name} - {self.price}"

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"


class Cart(models.Model):
    username = models.CharField(verbose_name='Имя',max_length=1555, unique=True)
    phone = models.CharField(verbose_name='Телефонный номер',max_length=50)
    address = models.CharField(verbose_name='Адрес',max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cart_item = models.TextField()
    
    def __str__(self):
        return f"{self.username} {self.phone} {self.total_price}"

    class Meta:
        verbose_name = "Корзинка"
        verbose_name_plural = "Корзинки"
        
