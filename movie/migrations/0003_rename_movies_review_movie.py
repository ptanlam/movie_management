# Generated by Django 3.2.6 on 2021-08-13 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20210813_1927'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='movies',
            new_name='movie',
        ),
    ]