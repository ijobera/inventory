# Generated by Django 2.0.4 on 2018-04-29 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='product_name',
            new_name='products_name',
        ),
    ]
