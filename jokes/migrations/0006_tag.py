# Generated by Django 5.2 on 2025-04-07 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0005_alter_category_options_alter_joke_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
