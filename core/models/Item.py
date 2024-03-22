from django.db import models
from django.conf import settings


class Item(models.Model):
    idItem = models.AutoField(
        db_column='id_item',
        primary_key=True
    )
    name = models.CharField(
        db_column='name',
        max_length=200,
    )
    description = models.CharField(
        db_column='description',
        max_length=200,
    )
    price = models.IntegerField(
        db_column='price',
    )
    image = models.CharField(
        db_column='image',
        max_length=500,
        default='https://womensfitness.co.uk/wp-content/uploads/sites/3/2022/11/Shutterstock_1675475479.jpg?w=900'
    )
    usuarioAdicion = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Usuario creador',
        db_column='usuario_adicion',
        related_name='usuario_adicion',
        blank=True
    )
    usuarioModificacion = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Usuario modificador',
        db_column='usuario_modificacion',
        related_name='usuario_modificacion',
        null=True,
        blank=True
    )
    fechaAdicion = models.DateTimeField(
        verbose_name='Fecha creación',
        auto_now_add=True,
        db_column='fecha_adicion',
        editable=False
    )
    fechaModificacion = models.DateTimeField(
        verbose_name='Fecha modificación',
        auto_now=True,
        db_column='fecha_modificacion',
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'MAE_ITEM'
