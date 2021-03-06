# Generated by Django 2.0.7 on 2018-08-14 13:50

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0040_articleconstants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interactiontype',
            name='default_description_en',
            field=wagtail.core.fields.RichTextField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='interactiontype',
            name='default_description_es',
            field=wagtail.core.fields.RichTextField(blank=True, max_length=300),
        ),
    ]
