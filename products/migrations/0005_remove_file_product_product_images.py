# Generated by Django 4.0.2 on 2022-02-06 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_product_images_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(to='products.File'),
        ),
    ]
