# Generated by Django 2.2.13 on 2020-10-11 19:33

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('projects', '0004_auto_20201011_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlatPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('headers', wagtail.core.fields.StreamField([('h_hero', wagtail.core.blocks.StructBlock([('slide_image', wagtail.images.blocks.ImageChooserBlock(blank=False, help_text='Großes, hochauflösendes Titelbild', required=True))], icon='image'))])),
                ('sections', wagtail.core.fields.StreamField([('s_info', wagtail.core.blocks.StructBlock([('thumbnail_image', wagtail.images.blocks.ImageChooserBlock(blank=False, help_text='Großes, hochauflösendes Titelbild', required=True)), ('info_text', wagtail.core.blocks.RichTextBlock(help_text='Info-Text', label='Text', required=False))], icon='fa-info')), ('s_contentcenter', wagtail.core.blocks.StructBlock([('content_center_head', wagtail.core.blocks.CharBlock(help_text='Content-Center Header', required=False)), ('content_center_lead', wagtail.core.blocks.CharBlock(help_text='Content-Center Untertitel', required=False)), ('content_center_text', wagtail.core.blocks.RichTextBlock(help_text='Content-Center Text', label='Text', required=False))], icon='fa-info')), ('s_contentright', wagtail.core.blocks.StructBlock([('content_right_img', wagtail.images.blocks.ImageChooserBlock(help_text='Content-Right Titelbild', required=False)), ('content_right_head', wagtail.core.blocks.CharBlock(help_text='Content-Right Header', required=False)), ('content_right_lead', wagtail.core.blocks.CharBlock(help_text='Content-Right Untertitel', required=False)), ('content_right_text', wagtail.core.blocks.RichTextBlock(help_text='Content-Right Text', label='Text', required=False))], icon='fa-info')), ('s_contentleft', wagtail.core.blocks.StructBlock([('content_left_img', wagtail.images.blocks.ImageChooserBlock(help_text='Content-Left Titelbild', required=False)), ('content_left_head', wagtail.core.blocks.CharBlock(help_text='Content-Left Header', required=False)), ('content_left_lead', wagtail.core.blocks.CharBlock(help_text='Content-Left Untertitel', required=False)), ('content_left_text', wagtail.core.blocks.RichTextBlock(help_text='Content-Left Text', label='Text', required=False))], icon='fa-info'))], blank=True, null=True)),
                ('gallery', wagtail.core.fields.StreamField([('g_gallery', wagtail.core.blocks.StructBlock([('gallery_image', wagtail.images.blocks.ImageChooserBlock(blank=False, help_text='Galerie-Bild', required=True))], icon='fa-info'))], blank=True, null=True)),
                ('token', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]