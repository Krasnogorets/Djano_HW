# Generated by Django 5.0.1 on 2024-02-11 19:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0008_alter_product_qts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]