# Generated by Django 3.1.6 on 2022-08-12 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_shares'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shares',
            options={'ordering': ['user2'], 'verbose_name': 'Поширені', 'verbose_name_plural': 'Поширені'},
        ),
    ]
