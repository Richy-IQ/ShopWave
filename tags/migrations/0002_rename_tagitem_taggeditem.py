# Generated by Django 4.2.5 on 2023-09-21 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TagItem',
            new_name='TaggedItem',
        ),
    ]