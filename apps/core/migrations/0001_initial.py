# Generated by Django 5.0.4 on 2024-04-23 11:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Names')),
                ('dni', models.CharField(max_length=10, unique=True, verbose_name='DNI')),
                ('date_joined', models.DateField(default=datetime.datetime(2024, 4, 23, 8, 47, 5, 624838), verbose_name='Date joined')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Date created')),
                ('age', models.PositiveIntegerField(default=0)),
                ('salary', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('state', models.BooleanField(default=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/%Y/%m/%d/')),
                ('cv', models.FileField(upload_to='cvs/%Y/%m/%d/')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
                'db_table': 'employee',
                'ordering': ['id'],
            },
        ),
    ]
