# Generated by Django 3.2.9 on 2022-03-13 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(to='products.Product'),
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
