# Generated by Django 3.2.19 on 2023-11-14 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stfcda', '0004_members_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='fb',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='members',
            name='lk',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='members',
            name='x',
            field=models.URLField(null=True),
        ),
    ]
