# Generated by Django 2.0.7 on 2018-08-07 08:03

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180807_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexblurb',
            name='section_content',
            field=wagtail.core.fields.StreamField([('text', wagtail.core.blocks.RichTextBlock()), ('partners', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(blank=True, max_length=25)), ('link', wagtail.core.blocks.CharBlock(blank=True, max_length=255)), ('logo', wagtail.images.blocks.ImageChooserBlock())])))], blank=True),
        ),
    ]
