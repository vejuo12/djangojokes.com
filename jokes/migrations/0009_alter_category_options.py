# Generated by Django 5.2 on 2025-04-07 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0008_alter_tag_options_alter_joke_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['category'], 'verbose_name_plural': 'Categories'},
        ),
    ]
