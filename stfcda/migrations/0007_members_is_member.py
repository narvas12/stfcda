# Generated by Django 3.2.19 on 2023-11-16 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stfcda', '0006_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='is_member',
            field=models.BooleanField(default=False),
        ),
    ]
