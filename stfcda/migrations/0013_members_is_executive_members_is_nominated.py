# Generated by Django 4.2.5 on 2023-12-19 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stfcda', '0012_delete_customcss'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='is_executive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='members',
            name='is_nominated',
            field=models.BooleanField(default=False),
        ),
    ]
