# Generated by Django 2.1.5 on 2019-04-12 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    def set_my_defaults(apps, schema_editor):
        ArticlePages = apps.get_model('article', 'ArticlePage')
        for article in ArticlePages.objects.all().iterator():
            article.is_published_en = True
            article.is_published_es = False
            article.save()

    def reverse_func(apps, schema_editor):
        pass  # code for reverting migration, if any

    dependencies = [
        ('article', '0071_auto_20190310_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepage',
            name='is_published_en',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='articlepage',
            name='is_published_es',
            field=models.BooleanField(null=True),
        ),
        migrations.RunPython(set_my_defaults, reverse_func),
        migrations.AlterField(
            model_name='articlepage',
            name='is_published_en',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='articlepage',
            name='is_published_es',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]