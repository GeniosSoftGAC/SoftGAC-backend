# Generated by Django 3.2.9 on 2022-03-20 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('primer_nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('products', models.ManyToManyField(blank=True, related_name='product_list', to='products.Product')),
            ],
            options={
                'ordering': ['-fecha_creacion'],
            },
        ),
    ]
