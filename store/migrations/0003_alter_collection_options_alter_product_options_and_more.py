# Generated by Django 4.2.5 on 2023-09-19 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['title']},
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='First_name',
            new_name='first_name',
        ),
    ]
