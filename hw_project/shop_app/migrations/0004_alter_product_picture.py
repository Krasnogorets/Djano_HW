# Generated by Django 5.0.1 on 2024-02-11 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0003_alter_product_description_alter_product_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
