# Generated by Django 2.2.13 on 2020-10-14 11:40

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_flatpage_buy_or_rent'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectspage',
            name='location_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Ortsname (z.B. Villach-Landskron)'),
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='available',
            field=models.BooleanField(verbose_name='Verfügbar'),
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='buy_or_rent',
            field=models.CharField(choices=[('RENT', 'Miete'), ('BUY', 'Kauf')], default='RENT', max_length=2, verbose_name='Mieten oder Kaufen?'),
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='ground_plan',
            field=wagtail.core.fields.StreamField([('p_groundplan', wagtail.core.blocks.StructBlock([('ground_plan', wagtail.images.blocks.ImageChooserBlock(blank=False, help_text='Grundriss', required=True))], icon='fa-info'))], blank=True, null=True, verbose_name='Grundrissplan'),
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='price',
            field=models.IntegerField(null=True, verbose_name='Preis'),
        ),
        migrations.AlterField(
            model_name='projectspage',
            name='buy_available',
            field=models.BooleanField(verbose_name='Kaufmöglichkeit'),
        ),
        migrations.AlterField(
            model_name='projectspage',
            name='coordinates',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Standpunkt (Koordinaten, z.B. Beispiel: 46.6120061,13.916085)'),
        ),
        migrations.AlterField(
            model_name='projectspage',
            name='flats',
            field=wagtail.core.fields.StreamField([('f_flats', wagtail.core.blocks.StructBlock([('flat', wagtail.core.blocks.PageChooserBlock(help_text='Wohneinheit im Gebäude', required=False))], icon='fa-info'))], blank=True, null=True, verbose_name='Wohneinheiten-Pages'),
        ),
        migrations.AlterField(
            model_name='projectspage',
            name='price_max',
            field=models.IntegerField(blank=True, null=True, verbose_name='Preis der teuersten Einheit (leer lassen wenn nur eine Einheit vorhanden ist)'),
        ),
        migrations.AlterField(
            model_name='projectspage',
            name='price_min',
            field=models.IntegerField(null=True, verbose_name='Preis der billigsten Einheit'),
        ),
        migrations.AlterField(
            model_name='projectspage',
            name='rent_available',
            field=models.BooleanField(verbose_name='Mietmöglichkeit'),
        ),
    ]
