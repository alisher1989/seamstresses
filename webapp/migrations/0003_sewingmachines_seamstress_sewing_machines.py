# Generated by Django 4.1.1 on 2022-09-08 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_seamstress_price_per_product_seamstress_total_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SewingMachines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название швейной машины')),
            ],
        ),
        migrations.AddField(
            model_name='seamstress',
            name='sewing_machines',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sewing_machines_rel', to='webapp.sewingmachines'),
        ),
    ]
