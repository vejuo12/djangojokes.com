# Generated by Django 5.2 on 2025-04-07 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0006_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='joke',
            name='tags',
            field=models.ManyToManyField(to='jokes.tag'),
        ),
    ]
