# Generated by Django 4.2.2 on 2023-06-19 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_rename_item_item_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='creado_el_dia',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='descripcion',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='esta_vendido',
            new_name='is_sold',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='precio',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='item',
            name='creado_por',
        ),
    ]
