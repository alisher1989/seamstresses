from django.db import models


class Seamstress(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    surname = models.CharField(max_length=200, verbose_name='Фамилия')
    total = models.IntegerField(verbose_name='Количество товаров', null=True)
    price_per_product = models.IntegerField(verbose_name='Цена за каждый продукт', null=True)
    total_price = models.IntegerField(verbose_name='Общая стоимость работы', null=True)
    sewing_machines = models.ForeignKey('SewingMachines', on_delete=models.CASCADE,
                                        related_name='sewing_machines_rel', null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.total_price = self.total * self.price_per_product
        super(Seamstress, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Швея'
        verbose_name_plural = 'Швеи'


class SewingMachines(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название швейной машины')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Швейная машина'
        verbose_name_plural = 'Швейные машины'




