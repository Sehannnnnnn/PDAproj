# Generated by Django 3.1.7 on 2021-03-31 13:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0004_remove_kakaotextfile_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='kakaotextfile',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='kakaotextfile',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
