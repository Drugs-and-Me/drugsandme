# Generated by Django 2.1 on 2018-12-02 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0063_auto_20181130_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleconstants',
            name='default_share_blurb_en',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='articleconstants',
            name='default_share_blurb_es',
            field=models.TextField(blank=True),
        ),
    ]
