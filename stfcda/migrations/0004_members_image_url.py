# Generated by Django 3.2.19 on 2023-11-14 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stfcda', '0003_members_is_trustee'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='image_url',
            field=models.URLField(null=True),
        ),
    ]
