# Generated by Django 2.0.7 on 2018-08-06 12:34

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0022_auto_20180806_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(to='article.ArticleCategory'),
        ),
    ]
