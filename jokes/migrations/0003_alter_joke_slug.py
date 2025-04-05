# Generated by Django 5.1.6 on 2025-04-04 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0002_joke_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joke',
            name='slug',
            field=models.SlugField(default='foo', editable=False, unique=True),
            preserve_default=False,
        ),
    ]
