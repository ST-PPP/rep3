# Generated by Django 4.2.13 on 2024-06-03 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0002_alter_table_column1'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Table',
            new_name='Product',
        ),
    ]
