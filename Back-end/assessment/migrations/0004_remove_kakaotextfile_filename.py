# Generated by Django 3.1.7 on 2021-03-31 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0003_kakaotextfile_filename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kakaotextfile',
            name='filename',
        ),
    ]
