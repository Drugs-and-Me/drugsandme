# Generated by Django 2.0.9 on 2018-10-08 20:49

import colorfield.fields
from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogindexpage_colour'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='colour',
            field=colorfield.fields.ColorField(default='#bbcee5', max_length=18),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='intro',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
