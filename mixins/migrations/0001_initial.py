# Generated by Django 4.0.2 on 2022-02-03 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('code', models.CharField(blank=True, max_length=15, verbose_name='Código')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('meta', models.TextField(verbose_name='Metadata')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mixins.listtype', verbose_name='Tipo de lista padre')),
            ],
            options={
                'verbose_name': 'Tipo de lista',
                'verbose_name_plural': 'Tipos de listas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('code', models.CharField(blank=True, max_length=15, verbose_name='Código')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('meta', models.TextField(verbose_name='Metadata')),
                ('list_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mixins.listtype', verbose_name='Elemento de la lista')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mixins.listitem', verbose_name='Elemento padre')),
            ],
            options={
                'verbose_name': 'Elemento de la lista',
                'verbose_name_plural': 'Elementos de la lista',
                'ordering': ['id'],
            },
        ),
    ]
