# Generated by Django 2.0.4 on 2018-04-29 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20180429_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_left',
            field=models.IntegerField(default=0),
        ),
    ]
