# Generated by Django 2.2.6 on 2019-11-04 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0004_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='apellido',
            field=models.CharField(max_length=200),
        ),
    ]
