# Generated by Django 2.0.7 on 2018-08-13 12:57

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0036_auto_20180813_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interactiontype',
            name='default_description_en',
            field=wagtail.core.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='interactiontype',
            name='default_description_es',
            field=wagtail.core.fields.RichTextField(),
        ),
    ]
