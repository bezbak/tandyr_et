# Generated by Django 4.2.5 on 2023-10-05 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_remove_cartitem_cart_cart_cart_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cart_item',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
        migrations.AddField(
            model_name='cart',
            name='cart_item',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]