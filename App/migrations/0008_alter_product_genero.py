# Generated by Django 4.2 on 2023-07-07 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_product_status_alter_product_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='genero',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
