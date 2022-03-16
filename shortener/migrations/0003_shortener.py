# Generated by Django 3.2.9 on 2022-03-08 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shortener', '0002_delete_shortener'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shortener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_URL', models.URLField()),
                ('shortened_URL', models.URLField()),
            ],
        ),
    ]
