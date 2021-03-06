# Generated by Django 2.0.7 on 2018-08-14 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0039_auto_20180813_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleConstants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_a_drug_en', models.CharField(blank=True, max_length=30)),
                ('select_a_drug_es', models.CharField(blank=True, max_length=30)),
                ('no_drug_selected_text_en', models.CharField(blank=True, max_length=255)),
                ('no_drug_selected_text_es', models.CharField(blank=True, max_length=255)),
                ('source_en', models.CharField(blank=True, max_length=15)),
                ('source_es', models.CharField(blank=True, max_length=15)),
            ],
        ),
    ]
