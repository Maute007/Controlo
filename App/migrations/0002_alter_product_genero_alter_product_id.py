# Generated by Django 4.2 on 2023-07-07 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='genero',
            field=models.CharField(choices=[('U', 'U'), ('M', 'M'), ('F', 'F')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
