# Generated by Django 4.0.2 on 2022-02-06 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_file_created_remove_file_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
