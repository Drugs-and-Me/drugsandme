# Generated by Django 2.0.7 on 2018-09-25 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0045_auto_20180916_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articletipsen',
            name='front_text',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='articletipses',
            name='front_text',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
