# Generated by Django 3.2.9 on 2022-03-08 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_shortener'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shortener',
            new_name='Link',
        ),
        migrations.RenameField(
            model_name='link',
            old_name='original_URL',
            new_name='original_link',
        ),
        migrations.RenameField(
            model_name='link',
            old_name='shortened_URL',
            new_name='shortened_link',
        ),
    ]
