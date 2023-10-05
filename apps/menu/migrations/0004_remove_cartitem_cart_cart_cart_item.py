# Generated by Django 4.2.5 on 2023-10-05 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_remove_cartitem_cart_cartitem_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.AddField(
            model_name='cart',
            name='cart_item',
            field=models.ManyToManyField(related_name='cart_items', to='menu.cartitem', verbose_name='Корзина'),
        ),
    ]