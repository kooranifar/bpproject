# Generated by Django 2.1.5 on 2019-02-10 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileuploader', '0004_picture_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
