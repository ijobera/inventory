# Generated by Django 2.0.4 on 2018-04-29 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20180429_1318'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Items',
            new_name='Item',
        ),
    ]