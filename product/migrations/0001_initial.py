# Generated by Django 2.1.7 on 2019-12-04 19:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=15)),
                ('trading_place', models.TextField()),
                ('status', models.CharField(max_length=30)),
                ('price', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='img/')),
                ('cart', models.ManyToManyField(related_name='_product_cart_+', to=settings.AUTH_USER_MODEL)),
                ('wish', models.ManyToManyField(related_name='_product_wish_+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
