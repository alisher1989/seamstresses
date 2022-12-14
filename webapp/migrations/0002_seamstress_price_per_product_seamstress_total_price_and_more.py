# Generated by Django 4.1.1 on 2022-09-08 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seamstress',
            name='price_per_product',
            field=models.IntegerField(null=True, verbose_name='Цена за каждый продукт'),
        ),
        migrations.AddField(
            model_name='seamstress',
            name='total_price',
            field=models.IntegerField(null=True, verbose_name='Общая стоимость работы'),
        ),
        migrations.AlterField(
            model_name='seamstress',
            name='total',
            field=models.IntegerField(null=True, verbose_name='Количество товаров'),
        ),
    ]
