# Generated by Django 4.2.6 on 2023-10-18 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='picture',
        ),
    ]
