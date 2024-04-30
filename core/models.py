from django.db import models
from datetime import datetime

from django.forms import model_to_dict
from django.utils import timezone

gender_choices = [
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('NB', 'No binario'),
    ('OT', 'Otro'),
    ('ND', 'Prefiero no decir'),
]


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Names', unique=True)
    description = models.CharField(max_length=300, verbose_name='Description', blank=True, null=True)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']
        db_table = 'category'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Names', unique=True)
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Image', upload_to='products/%Y/%m/%d/', null=True, blank=True)
    price = models.DecimalField(default=0, max_digits=9, decimal_places=2, verbose_name='Price')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['id']
        db_table = 'product'


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Names', unique=True)
    surname = models.CharField(max_length=100, verbose_name='Surname', unique=True)
    dni = models.CharField(max_length=10, verbose_name='DNI', unique=True)
    birth_date = models.DateField(default=timezone.now(), verbose_name='Birth Date', null=True, blank=True)
    address = models.CharField(max_length=100, verbose_name='Address', null=True, blank=True)
    gender = models.CharField(max_length=100, choices=gender_choices, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ['id']
        db_table = 'client'


class Sale(models.Model):
    client = models.ForeignKey(Client, verbose_name='Client', on_delete=models.CASCADE)
    date_joined = models.DateField(default=timezone.now(), verbose_name='Date Joined', null=True, blank=True)
    subtotal = models.DecimalField(default=0, max_digits=9, decimal_places=2, verbose_name='Subtotal')
    iva = models.DecimalField(default=0, max_digits=9, decimal_places=2, verbose_name='IVA')
    total = models.DecimalField(default=0, max_digits=9, decimal_places=2, verbose_name='Total')

    def __str__(self):
        self.client.name

    class Meta:
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'
        ordering = ['id']
        db_table = 'sale'


class DetailSale(models.Model):
    sale = models.ForeignKey(Sale, verbose_name='Sale', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Product', on_delete=models.CASCADE)
    price = models.DecimalField(default=0, max_digits=9, decimal_places=2, verbose_name='Price')
    quantity = models.IntegerField(default=0, verbose_name='Quantity')
    subtotal = models.DecimalField(default=0, max_digits=9, decimal_places=2, verbose_name='Subtotal')

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Detail Sale'
        verbose_name_plural = 'Detail Sale'
        ordering = ['id']
        db_table = 'detail_sale'
