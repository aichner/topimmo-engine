# Generated by Django 2.2.13 on 2020-12-11 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20201014_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatpage',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=11, null=True, verbose_name='Preis'),
        ),
    ]
