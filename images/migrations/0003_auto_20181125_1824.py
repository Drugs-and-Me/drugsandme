# Generated by Django 2.1 on 2018-11-25 18:24

from django.db import migrations


# https://stackoverflow.com/questions/41931590/data-migration-of-image-model
def forward_func(apps, schema_editor):
    wagtail_image_model = apps.get_model('wagtailimages', 'Image')
    new_image_model = apps.get_model('images', 'CustomImage')
    db_alias = schema_editor.connection.alias
    new_images = []
    for image in wagtail_image_model.objects.all():
        new_images.append(new_image_model(
            id=image.id,
            title=image.title,
            file=image.file,
            width=image.width,
            height=image.height,
            created_at=image.created_at,
            focal_point_x=image.focal_point_x,
            focal_point_y=image.focal_point_y,
            focal_point_width=image.focal_point_width,
            focal_point_height=image.focal_point_height,
            file_size=image.file_size,
            collection=image.collection,
            uploaded_by_user=image.uploaded_by_user,
        ))
    new_image_model.objects.using(db_alias).bulk_create(new_images)


def reverse_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    extended_image_model = apps.get_model('images', 'CustomImage')
    db_alias = schema_editor.connection.alias
    # Delete all images created in the new model
    extended_image_model.objects.using(db_alias).all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_customimage_description'),
    ]

    operations = [
        migrations.RunPython(forward_func, reverse_func),
    ]
