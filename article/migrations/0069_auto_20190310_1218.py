# Generated by Django 2.1 on 2019-03-10 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0068_auto_20190310_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammemberdetails',
            name='profile_picture',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
